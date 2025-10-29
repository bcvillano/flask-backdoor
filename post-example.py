import requests

IP_ADDR = "127.0.0.1"
PORT = 8912

data = {"id":"example","message":"This is a test!"}
r = requests.post(f"http://{IP_ADDR}:{PORT}/msg",json=data)
print(r.status_code)