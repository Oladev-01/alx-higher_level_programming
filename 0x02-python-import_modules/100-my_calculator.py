#!/usr/bin/python3
from calculator_1 import add, mul, sub, div
from sys import argv, exit
if __name__ == "__main__":
    args_len = len(argv)
    if args_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] != '+' and argv[2] != '-' and argv[2] != '*' and argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a, b = int(argv[1]), int(argv[3])
    if argv[2] == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif argv[2] == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif argv[2] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif argv[2] == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    exit(0)
