#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiplo = []
    for num in my_list:
        multiplo.append(num % 2 == 0)
    return multiplo
