#!/usr/bin/python3
"""this module gets the last 10 commits made in a
github repo"""

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    req = requests.get(url, params={'per_page': 10})
    if req.status_code == 200:
        req = req.json()
        for commits in req:
            sha = commits['sha']
            author_name = commits['commit']['author']['name']
            print(f"{sha}: {author_name}")
