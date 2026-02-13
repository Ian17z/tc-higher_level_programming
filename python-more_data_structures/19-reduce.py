#!/usr/bin/python3
from functools import reduce
def calc_average(a_dictionary):
    total_salary = reduce(lambda acc, x: acc + x["salary"], a_dictionary, 0)
    total_age = reduce(lambda acc, x: acc + x["age"], a_dictionary, 0)
    average_salary = total_salary / len(a_dictionary)
    average_age = total_age / len(a_dictionary)
    return average_salary, average_age
