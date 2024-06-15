#!/usr/bin/python3
"""this module makes a POST request to a url"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        mail = sys.argv[2]
        req = requests.post(url, data={'email': mail})
        print(req.text)
