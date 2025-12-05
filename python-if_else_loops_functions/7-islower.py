#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord(c) <= ord('z')
print("a is {}".format("lower" if islower("a") == True else "upper"))
print("H is {}".format("lower" if islower("H") == True else "upper"))
print("A is {}".format("lower" if islower("A") == True else "upper"))
print("3 is {}".format("lower" if islower("3") == True else "upper"))
print("g is {}".format("lower" if islower("g") == True else "upper"))
