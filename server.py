import http.server
import socketserver
from io import BytesIO
from os import curdir
PORT = 8080

"""
Machine IDs:
0: Washer 1
1: Washer 2
2: Washer 3
3: Dryer 1
4: Dryer 2
5: Dryer 3
"""


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        file = open(curdir + "/index.html", 'rb')
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(file.read())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
