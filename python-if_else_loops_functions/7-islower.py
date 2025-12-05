#!/usr/bin/python3
def islower(c):
    if c >= 'a' and c <= 'z':
        return True
    return False
print(islower('a'))  # True
print(islower('Z'))  # False
print(islower('m'))  # True
print(islower('1'))  # False
