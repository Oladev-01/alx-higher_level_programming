#!/usr/bin/python3
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        mail = sys.argv[2]
        value = {"email": mail}
        data = urlencode(value)
        data = data.encode('utf-8')
        req = Request(url, data=data)
        with urlopen(req) as response:
            resp = response.read().decode('utf-8')
            print(resp)
