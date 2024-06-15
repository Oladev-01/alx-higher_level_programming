#!/bin/bash
# trying to make the server send the response "You got me!"
curl -X POST -H "{Origin: You got me!}" "$1"
