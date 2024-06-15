#!/usr/bin/python3
"""this module gets the X-Request-Id header in the response generated
as a result of a fetch request to a given url"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        req = requests.get(url)
        print(req.headers.get('X-Request-Id'))
