#!/bin/bash
# this script prompt the ul to return all the acceptable HTTP methods it allows
echo $(curl -s -i -X OPTIONS "$1" | grep "Allow:" | sed 's/Allow: //')
