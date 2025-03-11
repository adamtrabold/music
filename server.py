from flask import Flask, send_from_directory, make_response
import os
import time

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/')
def serve_index():
    response = make_response(send_from_directory('.', 'index.html'))
    return response

@app.route('/<path:path>')
def serve_file(path):
    response = make_response(send_from_directory('.', path))
    if path.endswith(('.css', '.js')):
        response.headers['ETag'] = str(int(time.time()))
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)