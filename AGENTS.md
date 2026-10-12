# 3M 讀書會 專案開發規範 (Workspace Rules)

## 部署與發布規範 (Deployment Rule)
- **嚴格禁止直接 `git push` 發布至 GitHub Pages**。
- 所有程式碼、資料結構（`timeline_data.json`、`timeline_data.js`）、相片處理與排版樣式變更，一律**僅在本地端** (`http://localhost:8080`) 完成並供使用者檢驗。
- 只有在使用者於本機預覽確認無誤，並**明確發出「發布」、「部署」或「push」指令後**，才能執行 `git push origin main`。
