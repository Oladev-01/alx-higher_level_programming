#!/usr/bin/python3
"""this module sends a GET request to a url"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        try:
            req = Request(url)
            with urlopen(req) as response:
                resp = response.read().decode('utf-8')
                print(resp)
        except HTTPError as e:
            print(f"Error code: {e.code}")
