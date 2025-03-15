from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import logging
import socket

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SimpleDevServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.info(f"Received GET request from {self.client_address[0]} for path: {self.path}")
        try:
            # Add health check endpoint
            if self.path == '/health':
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'OK')
                return
            return SimpleHTTPRequestHandler.do_GET(self)
        except Exception as e:
            logging.error(f"Error serving request: {str(e)}")
            self.send_error(500, f"Internal server error: {str(e)}")

    def end_headers(self):
        # Disable caching for development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    server_address = ('0.0.0.0', 5000)
    try:
        # Log network interface information
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        logging.info(f'Server hostname: {hostname}')
        logging.info(f'Server local IP: {local_ip}')

        httpd = HTTPServer(server_address, SimpleDevServer)
        logging.info('Development server starting on port 5000...')
        logging.info(f'Server is ready to accept connections on {local_ip}:5000')
        httpd.serve_forever()
    except Exception as e:
        logging.error(f'Failed to start server: {str(e)}')
        raise