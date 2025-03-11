from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import hashlib
import time

class NoCacheHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add aggressive no-cache headers
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Last-Modified', 'Thu, 01 Jan 1970 00:00:00 GMT')
        self.send_header('Vary', '*')
        self.send_header('ETag', str(time.time()))  # Force unique ETag on every request
        SimpleHTTPRequestHandler.end_headers(self)

    def do_GET(self):
        # Force revalidation for all requests
        self.protocol_version = 'HTTP/1.1'
        SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, NoCacheHTTPRequestHandler)
    print('Serving on port 5000...')
    httpd.serve_forever()