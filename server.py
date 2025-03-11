from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import time
import urllib.parse

class NoCacheHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the path
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path

        # Add timestamp to static files
        if path.endswith(('.html', '.css', '.js')):
            timestamp = str(int(time.time()))
            if '?' in self.path:
                self.path = f"{self.path}&t={timestamp}"
            else:
                self.path = f"{self.path}?t={timestamp}"

        # Set headers before serving
        self.protocol_version = 'HTTP/1.1'
        SimpleHTTPRequestHandler.do_GET(self)

    def end_headers(self):
        # Add aggressive no-cache headers
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Last-Modified', 'Thu, 01 Jan 1970 00:00:00 GMT')
        self.send_header('Vary', '*')
        self.send_header('ETag', str(time.time()))
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    server_address = ('', 5000)
    httpd = HTTPServer(server_address, NoCacheHTTPRequestHandler)
    print('Serving on port 5000...')
    httpd.serve_forever()