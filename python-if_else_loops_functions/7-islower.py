#!/usr/bin/python3
def islower(c):
    if c >= 97 and c <= 122:
        return True
    else:
        return False
print("a is {}".format("lower" if islower(97) else "upper"))
print("H is {}".format("lower" if islower(72) else "upper"))
print("A is {}".format("lower" if islower(65) else "upper"))
print("3 is {}".format("lower" if islower(51) else "upper"))
print("g is {}".format("lower" if islower(103) else "upper"))
