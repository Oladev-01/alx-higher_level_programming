#!/bin/bash
# this script sends a GET request to a given URL and prints the body of a 200 status code
curl -s -o >(cat) -w "%{http_code}" "$1" | { read -r code; [ "$code" -eq 200 ] && cat; }
