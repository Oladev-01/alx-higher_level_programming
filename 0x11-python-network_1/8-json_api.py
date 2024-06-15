#!/usr/bin/python3
"""sending a POST request"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data={'q': letter})
    try:
        req = req.json()
        if req:
            print(f"[{req.get('id')}] {req.get('name')}")
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
