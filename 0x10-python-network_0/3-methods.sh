#!/bin/bash
# this script prompt the ul to return all the acceptable HTTP methods it allows
echo $(curl -s -X OPTIONS "$1")
