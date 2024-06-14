#!/bin/bash
# this script displays the status code of the response generated
curl -s -o /dev/null -w '%{http_code}' "$1"
