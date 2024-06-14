#!/bin/bash
# this script sends a GET request to a given URL and prints the body of a 200 status code
[ "$(curl -s -o /dev/stderr -w '%{http_code}' "$1")" -eq 200 ] && curl -s "$1"
