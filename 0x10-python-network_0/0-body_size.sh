#!/bin/bash
# this script runs curl on a given url and returns the size of the response body

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
fi

url="$1"
size=$(curl -s -o /dev/null -w '%{size_download}' "$url")
echo "$size"
