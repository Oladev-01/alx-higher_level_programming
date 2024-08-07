#!/usr/bin/python3
"""this module fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        data = response.read()
    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")
    print(f"\t- utf8: {data.decode('utf-8')}")
