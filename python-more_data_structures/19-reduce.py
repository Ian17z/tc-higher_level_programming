#!/usr/bin/python3
from functools import reduce
def calc_average(a_dictionary):
    count = len(a_dictionary)
    total_salary = reduce(
        lambda acc, item: acc + item["salary"],
        a_dictionary,
        0
    )
    total_age = reduce(
        lambda acc, item: acc + item["age"],
        a_dictionary,
        0
    )
    average_salary = total_salary / count if count else 0
    average_age = total_age / count if count else 0
    return average_salary, average_age
