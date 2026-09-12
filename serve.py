#!/usr/bin/env python3
"""Serve only DLSS5 FOR PS5's HTML on loopback. No third-party packages."""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

APP = Path(__file__).resolve().with_name("index.html")
HOST, PORT = "127.0.0.1", 8765


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.headers.get("Host") not in {f"{HOST}:{PORT}", f"localhost:{PORT}"}:
            self.send_error(403, "Invalid host")
            return
        if urlsplit(self.path).path not in {"/", "/index.html"}:
            self.send_error(404)
            return
        try:
            body = APP.read_bytes()
        except OSError:
            self.send_error(503, "index.html is unavailable")
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Permissions-Policy", "microphone=(), geolocation=()")
        self.end_headers()
        try:
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionResetError):
            pass


def main():
    if not APP.is_file():
        raise SystemExit("Keep serve.py next to index.html, then retry.")
    try:
        server = ThreadingHTTPServer((HOST, PORT), Handler)
    except OSError as error:
        raise SystemExit(f"Could not start localhost server: {error}") from error
    print(f"Open http://{HOST}:{PORT}/index.html")
    print("Only this app is served. Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
