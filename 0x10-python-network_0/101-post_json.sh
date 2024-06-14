#!/bin/bash
# this sends a POST request to the server
curl -X POST -s -H "Content-Type: application/json" -d @"$2" "$1"
