#!/usr/bin/python3
def uppercase(str):
    result = ""
    for c in str:
        if c >= 'a' and c <= 'z':
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
