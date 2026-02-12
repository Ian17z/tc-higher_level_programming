#!/usr/bin/python3
from functools import reduce
def calc_average(a_dictionary):
    total_age = reduce(lambda acc, emp: acc + emp["age"], a_dictionary, 0)
    total_salary = reduce(lambda acc, emp: acc + emp["salary"], a_dictionary, 0) 
    n = len(a_dictionary)
    print(total_age / n)
    print(total_salary / n)
