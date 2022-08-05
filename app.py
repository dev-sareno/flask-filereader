import os
from flask import Flask, Response

read_file = os.environ.get('APP_FILE_PATH', 'files/replaceme.txt')
if not os.path.isfile(read_file):
    raise FileNotFoundError(f'File not found {read_file}')

app = Flask(__name__)

@app.route("/")
def root():
    with open(read_file) as f:
        response = Response(f.read())
        response.headers['Content-Type'] = "text/plain"
        return response
