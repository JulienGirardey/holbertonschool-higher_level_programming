#!/usr/bin/python3

def islower(c):
    if c == '':
        return None
    if c < chr(97) or c > chr(122):
        return False
    else:
        return True
