import json, sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE = Path('.')
PHOTO_DIR = BASE / '3M 聚會照片'

folder_map = {
    '2015-10-18': ['FWD_2015'],
    '2016-04-20': ['FB training_2016-04-20'],
    '2018-04-28': ['3M 春酒_2018-04-28'],
    '2018-05-26': ['New retail_2018-5-26'],
    '2018-06-23': ['AI_2018-6-23'],
    '2018-07-28': ['Blockchain_2018-7-28'],
    '2018-12-15': ['Quantum Computing_2018-12-15'],
    '2019-07-27': ['UBI_2019-07-27'],
    '2021-07-31': ['小樹屋聚會_2021-7-31'],
    '2022-05-08': ['小樹屋聚會_2022-5-8'],
    '2023-04-23': ['彥伶 ChatGPT 交流_2023-4-23'],
    '2024-10-19': ['財務規劃 feat.劉耀元學長_2024-10-19'],
    '2025-08-16': ['川普關稅對全球影響_2025-08-16'],
    '2026-06-28': ['2026-06-28_AI agent sharing'],
    '2026-07-05': ['2026-07-05_平台生態系講座']
}

with open('timeline_data.json', encoding='utf-8') as f:
    events = json.load(f)

# 檢查是否已有 2026-06-28，若無則插入
has_0628 = any(e['date'] == '2026-06-28' for e in events)
if not has_0628:
    new_evt = {
        "id": "2026-06-28",
        "date": "2026-06-28",
        "year": "2026",
        "title": "AI Agent 應用實踐與自主代理人架構分享",
        "category": "科技趨勢",
        "speakers": ["Jerry"],
        "summary": "探討自主 AI Agent 工作流、多代理人協作機制與大語言模型落地實務，引領最新前瞻應用體驗。",
        "photo_folders": ["2026-06-28_AI agent sharing"],
        "media": [],
        "photos": []
    }
    # 插入在 2026-07-05 之前
    idx = next((i for i, e in enumerate(events) if e['date'] == '2026-07-05'), len(events) - 1)
    events.insert(idx, new_evt)
    print("✨ 已新增 2026-06-28 AI agent sharing 專題！")

total_photos = 0
total_gifs = 0

for e in events:
    d = e['date']
    if d in folder_map:
        e['photo_folders'] = folder_map[d]
        
    current_files = []
    for f_name in e.get('photo_folders', []):
        f_dir = PHOTO_DIR / f_name
        if f_dir.exists():
            for f in sorted(f_dir.iterdir()):
                if f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp', '.gif']:
                    current_files.append(f'3M 聚會照片/{f_name}/{f.name}')
                    
    for ex_dir in e.get('extra_image_dirs', []):
        ed = Path(ex_dir)
        if ed.exists():
            for f in sorted(ed.iterdir()):
                if f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.webp', '.gif']:
                    current_files.append(f'{ex_dir}/{f.name}'.replace('\\', '/'))
                    
    # 原本有自訂排序則保留存在者的順序
    old_urls = [m['url'] if isinstance(m, dict) else m for m in e.get('media', [])]
    ordered_files = [u for u in old_urls if u in current_files]
    for u in current_files:
        if u not in ordered_files:
            ordered_files.append(u)
            
    e['media'] = [{
        'url': u,
        'type': 'gif' if u.lower().endswith('.gif') else 'image',
        'name': Path(u).name
    } for u in ordered_files]
    e['photos'] = ordered_files
    
    gifs_count = sum(1 for m in e['media'] if m['type'] == 'gif')
    imgs_count = len(e['media']) - gifs_count
    total_photos += imgs_count
    total_gifs += gifs_count
    print(f"[{d}] {e['title'][:16]}: {imgs_count} 張相片, {gifs_count} 個 GIF (共 {len(e['media'])})")

# 依照日期排序
events.sort(key=lambda x: x['date'])

with open('timeline_data.json', 'w', encoding='utf-8') as f:
    json.dump(events, f, ensure_ascii=False, indent=2)

with open('timeline_data.js', 'w', encoding='utf-8') as f:
    f.write('window.TIMELINE_DATA = ' + json.dumps(events, ensure_ascii=False, indent=2) + ';\n')

print(f"\n✅ 重新整理完成！目前共 {len(events)} 場專題，{total_photos} 張精選相片、{total_gifs} 個動態 GIF。已精確同步刪減與新增結果！")
