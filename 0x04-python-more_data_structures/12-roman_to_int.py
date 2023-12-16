#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    else:
        rm_num = {'I': 1, 'V': 5, 'X': 10}
        rm_num.update({'L': 50, 'C': 100, 'D': 500, 'M': 1000})
        rt = 0
        for i in range(len(roman_string)):
            if i > 0 and rm_num[roman_string[i]] > rm_num[roman_string[i - 1]]:
                rt += rm_num[roman_string[i]] - 2 * rm_num[roman_string[i - 1]]
            else:
                rt += rm_num[roman_string[i]]
        return rt
