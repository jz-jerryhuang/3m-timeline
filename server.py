import http.server
import json
import os
import sys
from pathlib import Path

PORT = 8080
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

class TimelineHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 嚴格禁止快取，確保即時刷新最新資料
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_POST(self):
        if self.path == '/api/save':
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length)
                payload = json.loads(post_data.decode('utf-8', errors='replace'), strict=False)
                
                # 1. 寫入 timeline_data.json
                with open('timeline_data.json', 'w', encoding='utf-8') as f:
                    json.dump(payload, f, ensure_ascii=False, indent=2)
                
                # 2. 同步寫入 timeline_data.js
                with open('timeline_data.js', 'w', encoding='utf-8') as f:
                    f.write('window.TIMELINE_DATA = ' + json.dumps(payload, ensure_ascii=False, indent=2) + ';\n')
                
                count = len(payload) if isinstance(payload, list) else len(payload.get('events', []))
                response_body = json.dumps({'success': True, 'count': count}).encode('utf-8')
                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.send_header('Content-Length', str(len(response_body)))
                self.end_headers()
                self.wfile.write(response_body)
                print(f"💾 [SAVED] 成功儲存頂部設定與 {count} 筆時間軸資料並覆蓋本機檔案！")
            except Exception as e:
                err_msg = json.dumps({'success': False, 'error': str(e)}).encode('utf-8')
                self.send_response(500)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.send_header('Content-Length', str(len(err_msg)))
                self.end_headers()
                self.wfile.write(err_msg)
                print(f"❌ [ERROR] 儲存失敗: {e}")
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == '__main__':
    # 支援 Threading 避免單一連線卡死
    server = http.server.ThreadingHTTPServer(('', PORT), TimelineHTTPHandler)
    print(f"🚀 3M 讀書會伺服器已在 http://localhost:{PORT} 啟動（支援前端即時存檔）...")
    server.serve_forever()
