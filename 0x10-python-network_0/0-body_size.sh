#!/bin/bash
# this script runs curl on a given url and returns the size of the response body
echo $(curl -s -o /dev/null -w '%{size_download}' "$1")
