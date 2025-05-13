#!/usr/bin/python3
def roman_to_int(roman_string):
    dict_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    if not isinstance(roman_string, str) or roman_string == "":
        return 0
    count = 0
    i = 0
    for i in range(len(roman_string) - 1):
        if dict_num[roman_string[i]] < dict_num[roman_string[i + 1]]:
            count -= dict_num[roman_string[i]]
        else:
            count += dict_num[roman_string[i]]
    count += dict_num[roman_string[-1]]
    return count
