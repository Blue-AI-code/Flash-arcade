#!/usr/bin/env python3
"""Tiny local server. Run: python3 serve.py  then open http://localhost:8000"""
import http.server, socketserver, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
class H(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      '.wasm': 'application/wasm', '.js': 'text/javascript', '.swf': 'application/x-shockwave-flash'}
with socketserver.TCPServer(('', 8000), H) as s:
    print('Flash Arcade running at http://localhost:8000  (Ctrl+C to stop)')
    s.serve_forever()
