"""#1048 재현 서버: 8793. POST 를 기록한다."""
import http.server
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PAGE = open(os.path.join(HERE, "page.html"), encoding="utf-8").read().replace('action="javascript:window.__submitted=true"', 'action="/do"')


class Handler(http.server.BaseHTTPRequestHandler):
    def _send(self, body):
        data = body.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        self._send(PAGE)

    def do_POST(self):
        with open(os.path.join(HERE, "posts.log"), "a", encoding="utf-8") as handle:
            handle.write(self.path + "\n")
        self._send("<!doctype html><title>done</title><h1>requested</h1>")

    def log_message(self, *args):
        pass


http.server.ThreadingHTTPServer(("127.0.0.1", 8793), Handler).serve_forever()
