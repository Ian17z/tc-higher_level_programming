#!/usr/bin/python3
from functools import reduce
def calc_average(a_dictionary):
    values = list(a_dictionary.values())
    n = len(values)
    total_age = reduce(lambda acc, emp: acc + emp.get("age", 0), values, 0)
    total_salary = reduce(lambda acc, emp: acc + emp.get("salary", 0), values, 0)
    average_age = total_age / n
    average_salary = total_salary / n
    return average_salary, average_age
