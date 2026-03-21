import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    hostname = socket.gethostname()
    return f"Hello from DevOps intern! Host: {hostname}"

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/info')
def info():
    return jsonify({
        "app": "devops-demo",
        "version": "1.0.0",
        "environment": os.getenv("ENV", "production")
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)