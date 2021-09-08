import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from urls import url_patterns

port = 8000


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        api = list(filter(lambda x: self.path.split('?')[0] == x[0], url_patterns))
        if api:
            self.response(api[0][1])
        else:
            self.response_404()

    def do_POST(self):
        api = list(filter(lambda x: self.path.split('?')[0] == x[0], url_patterns))
        if api:
            self.response(api[0][1])
        else:
            self.response_404()

    def response(self, api):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Send the html message
        res = api(self)
        self.wfile.write(bytes(json.dumps(res), 'utf-8'))

    def response_404(self):
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        res = {
            "detail": "not found",
            "available_paths": list(map(lambda x: x[0], url_patterns))
        }
        self.wfile.write(bytes(json.dumps(res), 'utf-8'))


server = HTTPServer(('', port), MyHandler)
print('Started httpserver on port ', port)

# Wait forever for incoming http requests
server.serve_forever()
