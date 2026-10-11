import http.server
import sys

PORT = 8080
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

class TimelineHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # 嚴格禁止快取，確保即時刷新最新靜態資料
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

if __name__ == '__main__':
    server = http.server.ThreadingHTTPServer(('', PORT), TimelineHTTPHandler)
    print(f"🚀 3M 讀書會靜態伺服器已在 http://localhost:{PORT} 啟動...")
    server.serve_forever()
