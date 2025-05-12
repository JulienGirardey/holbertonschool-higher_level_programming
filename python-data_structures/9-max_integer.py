#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    int_max = my_list[0]
    for i in my_list:
        if i > int_max:
            int_max = i
    return int_max
