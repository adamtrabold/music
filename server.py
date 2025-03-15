from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SimpleDevServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.info(f"Received GET request for path: {self.path}")
        return SimpleHTTPRequestHandler.do_GET(self)

    def end_headers(self):
        # Disable caching for development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    server_address = ('0.0.0.0', 5000)
    try:
        httpd = HTTPServer(server_address, SimpleDevServer)
        logging.info('Development server starting on port 5000...')
        logging.info('Server is ready to accept connections')
        httpd.serve_forever()
    except Exception as e:
        logging.error(f'Failed to start server: {str(e)}')
        raise