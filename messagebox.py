#!/usr/bin/env python3

from flask import Flask, request
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

msg_logger = logging.getLogger("messagebox")
msg_logger.setLevel(logging.INFO)
handler = RotatingFileHandler(
    "messagebox.log",
    maxBytes=1_000_000,  # 1 MB
    backupCount=5
)
formatter = logging.Formatter("%(asctime)s %(message)s")
handler.setFormatter(formatter)
msg_logger.addHandler(handler)

@app.route('/msg', methods=['POST'])
def message():
    data = request.get_json()
    sender = data.get('id')
    msg = data.get('message')
    print(f"{sender}:{msg}")
    msg_logger.info(f"{sender}:{msg}")
    return "OK",200

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port=8912)