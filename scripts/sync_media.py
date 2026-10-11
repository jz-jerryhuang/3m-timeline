# -*- coding: utf-8 -*-
"""
scripts/sync_media.py
3M 讀書會 - 增量同步與媒體優化腳本 (Incremental Media Optimizer & Sync Tool)

功能：
1. 唯讀讀取「3M 聚會照片/」，絕對不修改或刪除原始母檔。
2. 增量轉檔至 photos_web/：
   - JPG/PNG -> 長邊 1600px WebP (quality=82) + 長邊 280px 膠捲縮圖 (quality=75, _thumb.webp)
   - GIF -> 首格擷取為 1280px WebP Poster (quality=82, _poster.webp) + 280px _thumb.webp (原始 GIF 燈箱播放)
3. 自動偵測與補齊既有活動資料夾中新加入的照片。
4. 偵測尚未關聯至 timeline_data.json 的新資料夾，並支援 --add-folder 一鍵建立新活動節點。
5. 雙向同步輸出 timeline_data.json 與 timeline_data.js (window.TIMELINE_DATA)。
"""

import sys
import os
import re
import json
import argparse
from pathlib import Path
from PIL import Image

BASE_DIR = Path('.')
PHOTO_DIR = BASE_DIR / '3M 聚會照片'
WEB_DIR = BASE_DIR / 'photos_web'
WEB_DIR.mkdir(parents=True, exist_ok=True)

IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def parse_date_and_title(folder_name: str):
    """
    從資料夾名稱智慧解析日期與標題：
    例如：
    - "2026-06-28_AI agent sharing" -> ("2026-06-28", "2026", "AI agent sharing")
    - "Blockchain_2018-7-28" -> ("2018-07-28", "2018", "Blockchain")
    - "2015-10-9 FWD 慶功宴" -> ("2015-10-09", "2015", "FWD 慶功宴")
    """
    date_pattern_1 = re.search(r'(\d{4})[-_](\d{1,2})[-_](\d{1,2})', folder_name)
    if date_pattern_1:
        y, m, d = date_pattern_1.groups()
        formatted_date = f"{int(y):04d}-{int(m):02d}-{int(d):02d}"
        clean_title = folder_name.replace(date_pattern_1.group(0), '').strip(' _-')
        return formatted_date, str(int(y)), clean_title or folder_name

    # 嘗試找年份
    year_match = re.search(r'(20\d{2})', folder_name)
    if year_match:
        y = year_match.group(1)
        return f"{y}-01-01", y, folder_name

    return "2026-01-01", "2026", folder_name

def optimize_single_file(orig_file: Path, force=False):
    """
    非破壞性媒體優化：
    - JPG/PNG -> 生成 1600px WebP + 280px 縮圖
    - GIF -> 生成 1280px 首格 Poster WebP + 280px 縮圖
    返回 (full_rel_path, thumb_rel_path, poster_rel_path, is_new)
    """
    rel_parts = orig_file.relative_to(PHOTO_DIR).parts
    if len(rel_parts) >= 2:
        subfolder = rel_parts[0]
    else:
        subfolder = 'misc'

    dest_sub_dir = WEB_DIR / subfolder
    dest_sub_dir.mkdir(parents=True, exist_ok=True)

    stem = orig_file.stem
    is_gif = orig_file.suffix.lower() == '.gif'

    web_full_file = dest_sub_dir / f"{stem}.webp"
    web_thumb_file = dest_sub_dir / f"{stem}_thumb.webp"
    web_poster_file = dest_sub_dir / f"{stem}_poster.webp"

    # 若檔案已存在且不強制重轉，直接沿用
    if not force:
        if is_gif and web_poster_file.exists() and web_thumb_file.exists():
            return (
                str(web_poster_file.as_posix()),
                str(web_thumb_file.as_posix()),
                str(web_poster_file.as_posix()),
                False
            )
        elif not is_gif and web_full_file.exists() and web_thumb_file.exists():
            return (
                str(web_full_file.as_posix()),
                str(web_thumb_file.as_posix()),
                "",
                False
            )

    try:
        with Image.open(orig_file) as im:
            # 1. 膠捲縮圖 280px
            im_thumb = im.copy()
            if is_gif:
                im_thumb.seek(0)
                im_thumb = im_thumb.convert('RGB')
            elif im_thumb.mode not in ('RGB', 'RGBA'):
                im_thumb = im_thumb.convert('RGB')
            im_thumb.thumbnail((280, 280), Image.Resampling.LANCZOS)
            im_thumb.save(web_thumb_file, 'WEBP', quality=75)

            if is_gif:
                # 2. 首格 Poster 1280px
                im_poster = im.copy()
                im_poster.seek(0)
                im_poster = im_poster.convert('RGB')
                im_poster.thumbnail((1280, 1280), Image.Resampling.LANCZOS)
                im_poster.save(web_poster_file, 'WEBP', quality=82)
                return (
                    str(web_poster_file.as_posix()),
                    str(web_thumb_file.as_posix()),
                    str(web_poster_file.as_posix()),
                    True
                )
            else:
                # 2. 高畫質大圖 1600px
                im_full = im.copy()
                if im_full.mode not in ('RGB', 'RGBA'):
                    im_full = im_full.convert('RGB')
                im_full.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
                im_full.save(web_full_file, 'WEBP', quality=82)
                return (
                    str(web_full_file.as_posix()),
                    str(web_thumb_file.as_posix()),
                    "",
                    True
                )
    except Exception as e:
        print(f"⚠️ 處理 {orig_file.name} 失敗: {e}")
        return ("", "", "", False)

def scan_all_folder_media(subfolder_name: str, force=False):
    """
    掃描特定照片子資料夾內所有圖檔，完成轉檔並回傳 media 物件清單
    """
    target_dir = PHOTO_DIR / subfolder_name
    if not target_dir.exists():
        return []

    media_list = []
    for f in sorted(target_dir.iterdir()):
        if f.is_file() and f.suffix.lower() in IMAGE_EXTS:
            full_p, thumb_p, poster_p, is_new = optimize_single_file(f, force=force)
            if not full_p:
                continue
            is_gif = f.suffix.lower() == '.gif'
            item = {
                "url": poster_p if is_gif else full_p,
                "type": "gif" if is_gif else "image",
                "name": f.name,
                "thumb": thumb_p,
                "original_url": str(f.as_posix())
            }
            if is_gif:
                item["poster"] = poster_p
                item["anim_url"] = str(f.as_posix())
            media_list.append(item)
    return media_list

def sync_data(force=False):
    """
    主同步函數：
    1. 掃描 timeline_data.json 所有活動，補齊新圖檔與轉檔
    2. 檢查是否有未關聯的聚會照片資料夾
    """
    json_path = Path('timeline_data.json')
    if not json_path.exists():
        print("❌ 找不到 timeline_data.json")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    events = data.get('events', [])
    used_folders = set()
    updated_files_count = 0
    total_media_count = 0

    print("🔍 [1/3] 正在比對既有活動與照片目錄...")

    for ev in events:
        folders = ev.get('photo_folders', [])
        for fld in folders:
            used_folders.add(fld)

        # 重新掃描既有 photo_folders，確保新放進來的照片也會被讀取
        existing_orig_names = {
            Path(m.get('original_url') or m.get('url', '')).name: m 
            for m in ev.get('media', [])
        }

        new_media_list = []
        for fld in folders:
            folder_path = PHOTO_DIR / fld
            if not folder_path.exists():
                continue
            for f in sorted(folder_path.iterdir()):
                if f.is_file() and f.suffix.lower() in IMAGE_EXTS:
                    total_media_count += 1
                    full_p, thumb_p, poster_p, is_new = optimize_single_file(f, force=force)
                    if is_new:
                        updated_files_count += 1
                        print(f"  ✨ [新轉檔] {fld}/{f.name}")
                    
                    is_gif = f.suffix.lower() == '.gif'
                    item = {
                        "url": poster_p if is_gif else full_p,
                        "type": "gif" if is_gif else "image",
                        "name": f.name,
                        "thumb": thumb_p,
                        "original_url": str(f.as_posix())
                    }
                    if is_gif:
                        item["poster"] = poster_p
                        item["anim_url"] = str(f.as_posix())
                    new_media_list.append(item)

        # 若原本有 extra_image_dirs 或無 folder 的特殊媒體，予以保留
        if not folders and ev.get('media'):
            for m in ev.get('media', []):
                total_media_count += 1
                orig_rel = m.get('original_url') or m.get('url')
                orig_file = BASE_DIR / orig_rel
                if orig_file.exists():
                    full_p, thumb_p, poster_p, is_new = optimize_single_file(orig_file, force=force)
                    if is_new:
                        updated_files_count += 1
                    m['thumb'] = thumb_p
                    m['original_url'] = str(orig_file.as_posix())
                    if orig_file.suffix.lower() == '.gif':
                        m['poster'] = poster_p
                        m['url'] = poster_p
                        m['anim_url'] = str(orig_file.as_posix())
                    else:
                        m['url'] = full_p
                new_media_list.append(m)

        if new_media_list:
            ev['media'] = new_media_list
            ev['photos'] = [m['url'] for m in new_media_list]

    # 寫回 JSON 與 JS
    print("💾 [2/3] 正在寫入 timeline_data.json 與 timeline_data.js...")
    with open('timeline_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    with open('timeline_data.js', 'w', encoding='utf-8') as f:
        f.write('window.TIMELINE_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n')

    print("🔎 [3/3] 檢查未歸檔的聚會資料夾...")
    all_disk_folders = {d.name for d in PHOTO_DIR.iterdir() if d.is_dir() and not d.name.startswith('.')}
    unlinked = sorted(list(all_disk_folders - used_folders))

    if unlinked:
        print(f"\n⚠️  發現 {len(unlinked)} 個尚未連結至 timeline_data.json 的相片資料夾：")
        for u in unlinked:
            cnt = len([p for p in (PHOTO_DIR / u).iterdir() if p.suffix.lower() in IMAGE_EXTS])
            dt, yr, title = parse_date_and_title(u)
            print(f"  📁 「{u}」 (內含 {cnt} 張圖檔)")
            print(f"     💡 快速加入指令: python scripts/sync_media.py --add-folder \"{u}\" --title \"{title}\"")
    else:
        print("🎉 所有相片資料夾皆已妥善歸檔！")

    print(f"\n✅ 同步完成！共納入 {total_media_count} 個媒體項目，本次增量壓製 {updated_files_count} 個新檔案。")

def add_folder_as_event(folder_name: str, title: str = None, category: str = "聚會紀實", speakers: list = None, summary: str = ""):
    """
    將尚未收錄的相片資料夾新增為一個 Timeline 活動節點
    """
    target_dir = PHOTO_DIR / folder_name
    if not target_dir.exists():
        print(f"❌ 找不到資料夾: {PHOTO_DIR / folder_name}")
        return

    parsed_date, parsed_year, parsed_title = parse_date_and_title(folder_name)
    event_title = title or parsed_title
    event_speakers = speakers or ["3M 全員"]

    media_items = scan_all_folder_media(folder_name)
    if not media_items:
        print(f"⚠️ 資料夾 {folder_name} 中未找到任何影像檔案！")

    new_event = {
        "id": parsed_date,
        "date": parsed_date,
        "year": parsed_year,
        "title": event_title,
        "category": category,
        "speakers": event_speakers,
        "summary": summary or f"{parsed_date} 讀書會聚會記錄：{event_title}。",
        "photo_folders": [folder_name],
        "media": media_items,
        "photos": [m["url"] for m in media_items]
    }

    # 讀取現有 data
    with open('timeline_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    events = data.get('events', [])
    
    # 檢查是否已存在該 id
    existing_idx = next((i for i, e in enumerate(events) if e.get('id') == parsed_date or folder_name in e.get('photo_folders', [])), None)
    if existing_idx is not None:
        print(f"🔄 發現已存在同日期/資料夾活動，更新既有節點: {events[existing_idx]['title']}")
        events[existing_idx] = new_event
    else:
        events.append(new_event)
        # 按日期正序排列
        events.sort(key=lambda x: x.get('date', ''))
        print(f"➕ 已成功加入新節點: [{parsed_date}] {event_title} (共 {len(media_items)} 張相片)")

    data['events'] = events

    with open('timeline_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    with open('timeline_data.js', 'w', encoding='utf-8') as f:
        f.write('window.TIMELINE_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n')

    print("🎉 資料已成功寫入 timeline_data.json 與 timeline_data.js！")

def main():
    parser = argparse.ArgumentParser(description="3M 讀書會時光軸媒體同步與發布工具")
    parser.add_argument('--force', action='store_true', help="強制重新轉檔所有 WebP 圖片")
    parser.add_argument('--add-folder', type=str, help="將指定的照片資料夾自動新增為時光軸活動節點")
    parser.add_argument('--title', type=str, help="新活動標題")
    parser.add_argument('--category', type=str, default="聚會紀實", help="新活動分類")
    parser.add_argument('--speakers', type=str, help="新活動講者 (以逗號分隔，例如: 'Jerry, Vickie')")
    parser.add_argument('--summary', type=str, default="", help="新活動摘要內文")

    args = parser.parse_args()

    if args.add_folder:
        sp_list = [s.strip() for s in args.speakers.split(',')] if args.speakers else ["3M 全員"]
        add_folder_as_event(
            folder_name=args.add_folder,
            title=args.title,
            category=args.category,
            speakers=sp_list,
            summary=args.summary
        )
    else:
        sync_data(force=args.force)

if __name__ == '__main__':
    main()
