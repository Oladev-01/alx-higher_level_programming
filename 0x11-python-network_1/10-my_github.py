#!/usr/bin/python3
"""this module connects tries to connect
 to github via github api using the username and password parsed to
 the script"""

import requests
import sys


if __name__ == "__main__":
    username, password = sys.argv[1], sys.argv[2]
    url = "https://api.github.com/user"
    req = requests.get(url, auth=(username, password))
    if req.status_code == 200:
        req_json = req.json()
        print(req_json['id'])
    else:
        print("None")
