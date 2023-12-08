#!/usr/bin/python3
from sys import argv
a = 0
if __name__ == "__main__":
    for i in range(1, len(argv)):
        a += int(argv[i])

print("{}".format(a))
