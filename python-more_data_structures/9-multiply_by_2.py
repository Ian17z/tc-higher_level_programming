#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mult = {}
    for i in a_dictionary:
        mult[i] = a_dictionary[i] * 2
    return mult
