#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        if a or b == type(float()):
            return int(a + b)
    except:
        print('a must be an integer ou b must be an integer')
   
print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)