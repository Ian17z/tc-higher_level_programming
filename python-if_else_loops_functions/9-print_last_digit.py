#!/usr/bin/python3
def print_last_digit(number):
    return abs(number) % 10
r = print_last_digit(98)
print(r)
r = print_last_digit(0)
print(r)
r = print_last_digit(-1024)
print(r)
