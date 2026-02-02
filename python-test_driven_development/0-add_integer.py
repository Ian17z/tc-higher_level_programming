#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        a = int(a)
    except (TypeError, ValueError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (TypeError, ValueError):
        raise TypeError("b must be an integer")

    return a + b















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