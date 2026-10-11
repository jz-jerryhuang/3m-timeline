# -*- coding: utf-8 -*-
"""
Non-destructive media optimization script for 3M Timeline.
Reads originals from '3M 聚會照片' without modifying them.
Outputs web-optimized assets to 'photos_web'.
"""
import os
import json
import time
from pathlib import Path
from PIL import Image

BASE_DIR = Path('.')
PHOTO_DIR = BASE_DIR / '3M 聚會照片'
WEB_DIR = BASE_DIR / 'photos_web'
WEB_DIR.mkdir(parents=True, exist_ok=True)

with open('timeline_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

events = data.get('events', [])
total_media = sum(len(e.get('media', [])) for e in events)
print(f"Total media items to process: {total_media}", flush=True)

processed = 0
total_orig_bytes = 0
total_web_bytes = 0

t0 = time.time()

for ev in events:
    media_list = ev.get('media', [])
    for m in media_list:
        orig_rel_path = m.get('url', '')
        orig_file = BASE_DIR / orig_rel_path

        if not orig_file.exists():
            print(f"Warning: File not found: {orig_file}", flush=True)
            continue

        orig_size = orig_file.stat().st_size
        total_orig_bytes += orig_size

        # Determine destination folder inside photos_web
        # e.g. orig_rel_path = '3M 聚會照片/FWD_2015/1.jpg'
        # subfolder = 'FWD_2015'
        rel_parts = Path(orig_rel_path).parts
        if len(rel_parts) >= 3:
            subfolder = rel_parts[1]
        elif len(rel_parts) == 2:
            subfolder = 'root'
        else:
            subfolder = 'misc'

        dest_sub_dir = WEB_DIR / subfolder
        dest_sub_dir.mkdir(parents=True, exist_ok=True)

        stem = orig_file.stem
        is_gif = orig_file.suffix.lower() == '.gif'

        # Target filenames
        web_full_file = dest_sub_dir / f"{stem}.webp"
        web_thumb_file = dest_sub_dir / f"{stem}_thumb.webp"
        web_poster_file = dest_sub_dir / f"{stem}_poster.webp"

        # Web relative paths for JSON (using forward slashes)
        web_full_rel = str(web_full_file.as_posix())
        web_thumb_rel = str(web_thumb_file.as_posix())
        web_poster_rel = str(web_poster_file.as_posix())

        try:
            with Image.open(orig_file) as im:
                # 1. Thumbnail (Max 280x280) for filmstrip
                im_thumb = im.copy()
                if is_gif:
                    im_thumb.seek(0)
                    im_thumb = im_thumb.convert('RGB')
                elif im_thumb.mode not in ('RGB', 'RGBA'):
                    im_thumb = im_thumb.convert('RGB')
                
                im_thumb.thumbnail((280, 280), Image.Resampling.LANCZOS)
                im_thumb.save(web_thumb_file, 'WEBP', quality=75)
                total_web_bytes += web_thumb_file.stat().st_size

                if is_gif:
                    # 2. GIF Poster (Max 1280x1280, 1st frame)
                    im_poster = im.copy()
                    im_poster.seek(0)
                    im_poster = im_poster.convert('RGB')
                    im_poster.thumbnail((1280, 1280), Image.Resampling.LANCZOS)
                    im_poster.save(web_poster_file, 'WEBP', quality=82)
                    total_web_bytes += web_poster_file.stat().st_size

                    # Update media entry metadata
                    m['thumb'] = web_thumb_rel
                    m['poster'] = web_poster_rel
                    m['original_url'] = orig_rel_path
                    # For card display, use poster as fast preview
                    m['url'] = web_poster_rel
                    m['anim_url'] = orig_rel_path
                else:
                    # 3. Photo Full View (Max 1600x1600)
                    im_full = im.copy()
                    if im_full.mode not in ('RGB', 'RGBA'):
                        im_full = im_full.convert('RGB')
                    
                    im_full.thumbnail((1600, 1600), Image.Resampling.LANCZOS)
                    im_full.save(web_full_file, 'WEBP', quality=82)
                    total_web_bytes += web_full_file.stat().st_size

                    # Update media entry metadata
                    m['thumb'] = web_thumb_rel
                    m['original_url'] = orig_rel_path
                    m['url'] = web_full_rel

            processed += 1
            if processed % 10 == 0 or processed == total_media:
                print(f"Processed {processed}/{total_media} items...", flush=True)

        except Exception as e:
            print(f"Error processing {orig_file}: {e}", flush=True)

# Update data.photos arrays in each event as well
for ev in events:
    if 'media' in ev:
        ev['photos'] = [m['url'] for m in ev['media']]

# Write updated timeline_data.json
with open('timeline_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Write updated timeline_data.js
with open('timeline_data.js', 'w', encoding='utf-8') as f:
    f.write('window.TIMELINE_DATA = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n')

elapsed = time.time() - t0
orig_mb = total_orig_bytes / (1024 * 1024)
web_mb = total_web_bytes / (1024 * 1024)
ratio = (1 - (total_web_bytes / total_orig_bytes)) * 100 if total_orig_bytes > 0 else 0

print("\n" + "=" * 50, flush=True)
print(f"Optimization Complete in {elapsed:.1f}s!", flush=True)
print(f"Original Total Payload:  {orig_mb:.2f} MB", flush=True)
print(f"Optimized Web Payload:   {web_mb:.2f} MB", flush=True)
print(f"Total Bandwidth Reduced: {ratio:.1f}%", flush=True)
print("=" * 50, flush=True)
