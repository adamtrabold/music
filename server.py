from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class SimpleDevServer(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Disable caching for development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    server_address = ('0.0.0.0', 5001)
    httpd = HTTPServer(server_address, SimpleDevServer)
    print('Development server running on port 5001...')
    httpd.serve_forever()