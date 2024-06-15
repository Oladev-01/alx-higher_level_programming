#!/usr/bin/python3
"""this module accepts a url as argument and print
 the value of the X-Request-Id variable
 found in the header of the response"""

from urllib.request import Request, urlopen
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        req = Request(url)
        with urlopen(req) as response:
            x_request = response.headers.get('X-Request-Id')
            print(x_request)
