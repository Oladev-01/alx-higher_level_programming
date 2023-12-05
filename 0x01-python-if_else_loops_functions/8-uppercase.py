#!/usr/bin/python3
def uppercase(str):
    if not str:
        print("\"\"")
    else:
        total_string = ""
        for i in str:
            check = ord(i)
            if check in range(97, 123):
                conv_upper = chr(check - 32)
                total_string += conv_upper
            else:
                total_string += i
        print(total_string)
