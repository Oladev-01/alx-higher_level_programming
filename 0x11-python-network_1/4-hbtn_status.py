#!/usr/bin/python3
"""this module use the requests module to fetch a url"""

import requests


url = "https://alx-intranet.hbtn.io/status"
req = requests.get(url)
print("Body response:")
print(f"\t- type: {type(req.text)}")
print(f"\t- content: {req.text}")
