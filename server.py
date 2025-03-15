from flask import Flask, send_from_directory
import os
import logging
import socket

# Configure logging (from edited code)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__, static_url_path='')

@app.route('/health')
def health_check():
    return 'OK'

@app.route('/')
def root():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    try:
        # Log network interface information (from original code)
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        logging.info(f'Server hostname: {hostname}')
        logging.info(f'Server local IP: {local_ip}')
        
        logging.info('Starting Flask development server on port 5000...')
        app.run(host='0.0.0.0', port=5000, debug=True)
    except Exception as e:
        logging.error(f'Failed to start server: {str(e)}')
        raise