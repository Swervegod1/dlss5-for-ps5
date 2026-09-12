#!/usr/bin/env python3
"""Source integrity and loopback-server checks; not a browser or PS5 test."""
import ast
from collections import Counter
from html.parser import HTMLParser
import http.client
import importlib.util
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]


class Markup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.labels, self.script_sources = [], [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "label" and "for" in a:
            self.labels.append(a["for"])
        if tag == "script" and "src" in a:
            self.script_sources.append(a["src"])


class ProjectTests(unittest.TestCase):
    def test_markup_references(self):
        html = (ROOT / "index.html").read_text()
        markup = Markup()
        markup.feed(html)
        self.assertEqual([key for key, n in Counter(markup.ids).items() if n > 1], [])
        self.assertTrue(set(markup.labels) <= set(markup.ids))
        self.assertTrue(set(re.findall(r'\$\("([A-Za-z][A-Za-z0-9]*)"\)', html)) <= set(markup.ids))
        self.assertEqual(markup.script_sources, [])

    def test_javascript_syntax(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("Node.js not installed; JavaScript syntax check skipped")
        script = re.search(r"<script>(.*?)</script>", (ROOT / "index.html").read_text(), re.S).group(1)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "app.js"
            path.write_text(script)
            result = subprocess.run([node, "--check", str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_python_syntax(self):
        for path in ROOT.rglob("*.py"):
            ast.parse(path.read_text(), filename=str(path))

    def test_documentation_links(self):
        for doc in ROOT.glob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", doc.read_text()):
                if "://" not in target and not target.startswith("#"):
                    self.assertTrue((doc.parent / target.split("#")[0]).is_file(), f"Broken local link in {doc.name}: {target}")

    def test_server_restricts_routes_and_host(self):
        spec = importlib.util.spec_from_file_location("clarity_server", ROOT / "serve.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        server = module.ThreadingHTTPServer(("127.0.0.1", 0), module.Handler)
        module.PORT = server.server_port
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()

        def request(path, host=None):
            connection = http.client.HTTPConnection("127.0.0.1", server.server_port, timeout=3)
            headers = {} if host is None else {"Host": host}
            connection.request("GET", path, headers=headers)
            response = connection.getresponse()
            status, body, headers = response.status, response.read(), dict(response.getheaders())
            connection.close()
            return status, body, headers

        try:
            for path in ["/", "/index.html", "/index.html?demo=1"]:
                status, body, headers = request(path)
                self.assertEqual(status, 200)
                self.assertEqual(body, (ROOT / "index.html").read_bytes())
                self.assertEqual(headers["Cache-Control"], "no-store")
                self.assertEqual(headers["X-Frame-Options"], "DENY")
            for path in ["/README.md", "/../serve.py", "/%2e%2e/serve.py", "/missing"]:
                self.assertEqual(request(path)[0], 404)
            self.assertEqual(request("/", "untrusted.example")[0], 403)
        finally:
            server.shutdown()
            server.server_close()
            worker.join(timeout=3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
