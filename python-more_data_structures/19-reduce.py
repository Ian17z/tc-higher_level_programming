#!/usr/bin/python3
from functools import reduce
def calc_average(a_dictionary):
    n = len(a_dictionary)

    print(reduce(lambda a, b: a + b["age"], a_dictionary, 0) / n)
    print(reduce(lambda a, b: a + b["salary"], a_dictionary, 0) / n)
