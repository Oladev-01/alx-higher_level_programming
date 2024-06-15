#!/usr/bin/python3
"""this module fetches a url, displays its response body
or error code if >= 400"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        req = requests.get(url)
        if req.status_code >= 400:
            print(f"Error code: {req.status_code}")
        else:
            print(req.text)
