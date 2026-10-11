---
name: update-3m-timeline
description: >-
  3M 讀書會時光軸網頁內容維護與增量發布 SOP。當使用者在 Google 雲端硬碟「3M 聚會照片/」放入新照片、GIF 簡報，或需在網頁時光軸新增、修改讀書會活動專題（標題、講者、摘要、日期）並同步發布至 GitHub Pages 時使用此技能。
---

# 3M 讀書會時光軸內容更新與同步流程 (Runbook)

本流程專門處理「雲端硬碟放入新照片/新活動」到「GitHub Pages 網站正式上線」的自動化增量更新，嚴格維持**非破壞性**原則（絕對不更動母檔）。

---

## 核心架構與檔案清單

| 目錄 / 檔案 | 職責說明 |
| :--- | :--- |
| `3M 聚會照片/` | **原始母檔目錄 (唯讀)**。由成員或雲端硬碟上傳，包含原解析度相片與高解析 GIF。 |
| `photos_web/` | **網頁優化目錄 (WebP)**。供前端高速載入（1600px 大圖、280px 膠捲縮圖 `_thumb.webp`、GIF 靜態海報 `_poster.webp`）。 |
| `timeline_data.json` | 讀書會活動主資料庫（`hero` 統計資訊與 `events` 活動陣列）。 |
| `timeline_data.js` | 前端全域直接讀取的 JavaScript 格式資料（`window.TIMELINE_DATA`），免除瀏覽器快取與 CORS 限制。 |
| `scripts/sync_media.py` | 自動化增量壓製與事件建立工具。 |
| `index.html` | Vue 3 + Tailwind CSS 時光軸單頁應用，已整合 Manifesto 獨立宣言手稿風格。 |

---

## 標準作業流程 (SOP)

### 步驟 1：掃描相片庫與未收錄資料夾

在終端機執行：
```powershell
python scripts/sync_media.py
```
腳本將自動：
1. 比對現有活動，對既有資料夾內新增的相片自動產生 WebP 與縮圖。
2. 自動列出尚未收錄至時光軸的新資料夾與相片數量，並給出建議指令。

---

### 步驟 2：新增或修改讀書會活動

#### 情況 A：新增全新活動資料夾 (一鍵建立)
若雲端硬碟加入了如 `3M 聚會照片/2026-11-20_新主題/`：
```powershell
python scripts/sync_media.py --add-folder "2026-11-20_新主題" --title "主題名稱" --category "科技趨勢" --speakers "Jerry, Vickie" --summary "本次聚會探討..."
```
> **注意**：腳本會自動將新活動依 `date` 排序插入正確時間軸位置，並同步產出 `photos_web` 轉檔與更新 `timeline_data.js`。

#### 情況 B：微調活動文字 (摘要、講者或連結)
直接編輯 `timeline_data.json` 中對應的 event 物件，儲存後執行：
```powershell
python scripts/sync_media.py
```
此指令會自動將更新內容重新同步至 `timeline_data.js`。

---

### 步驟 3：本地即時預覽與檢查

若本地預覽伺服器已在背景運行 (`http://localhost:8080`)，直接重新整理瀏覽器檢驗：
- 檢查時光軸節點日期、順序是否正確。
- 檢查縮圖列（底片膠捲）是否顯示無破損。
- 點擊圖片展開全螢幕燈箱，確認高畫質大圖或 GIF 動態播放正常。

若本機伺服器未啟動，可透過以下指令開啟：
```powershell
python server.py
```

---

### 步驟 4：發布至 GitHub Pages

確認無誤後，提交變更並推送至 GitHub：
```powershell
git add timeline_data.json timeline_data.js photos_web/ scripts/
git commit -m "feat(timeline): 更新讀書會活動內容與照片"
git push origin main
```
推送至 `main` 分支後，GitHub Pages 會在 1~2 分鐘內自動更新：
- 🌐 線上公開網址：`https://jz-jerryhuang.github.io/3m-timeline/`

---

## 資料結構定義參考

每個 event 節點在 `timeline_data.json` 的標準規格：

```json
{
  "id": "2026-11-20",
  "date": "2026-11-20",
  "year": "2026",
  "title": "活動標題",
  "category": "科技趨勢",
  "speakers": ["講者 A", "講者 B"],
  "summary": "1~2 句精簡摘要，記錄本次聚會交流核心要點。",
  "photo_folders": [
    "2026-11-20_新主題"
  ],
  "media": [
    {
      "url": "photos_web/2026-11-20_新主題/P1.webp",
      "type": "image",
      "name": "P1.jpg",
      "thumb": "photos_web/2026-11-20_新主題/P1_thumb.webp",
      "original_url": "3M 聚會照片/2026-11-20_新主題/P1.jpg"
    },
    {
      "url": "photos_web/2026-11-20_新主題/anim.webp",
      "type": "gif",
      "name": "anim.gif",
      "thumb": "photos_web/2026-11-20_新主題/anim_thumb.webp",
      "original_url": "3M 聚會照片/2026-11-20_新主題/anim.gif",
      "poster": "photos_web/2026-11-20_新主題/anim_poster.webp",
      "anim_url": "3M 聚會照片/2026-11-20_新主題/anim.gif"
    }
  ],
  "photos": [
    "photos_web/2026-11-20_新主題/P1.webp",
    "photos_web/2026-11-20_新主題/anim_poster.webp"
  ]
}
```

---

## 注意事項與防呆機制

1. **嚴禁破壞母檔**：不要修改、更名或覆寫 `3M 聚會照片/` 內的任何原始檔案。
2. **GIF 效能控制**：GIF 檔案體積龐大，時光軸列表一律載入 `_poster.webp` 與 `_thumb.webp`，唯有在使用者點進燈箱時才載入 `anim_url`。
3. **強制重新轉檔**：如遇到圖檔旋轉問題或需強制重新產生特定資料夾 WebP，可加上 `--force` 參數：
   ```powershell
   python scripts/sync_media.py --force
   ```
