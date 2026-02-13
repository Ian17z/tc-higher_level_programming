#!/usr/bin/python3
from functools import reduce


def calc_average(a_dictionary):
    """Calcula a média de age e salary usando reduce"""

    values = a_dictionary.values()
    count = len(values)

    total_salary = reduce(
        lambda acc, item: acc + item["salary"],
        values,
        0
    )

    total_age = reduce(
        lambda acc, item: acc + item["age"],
        values,
        0
    )

    average_salary = total_salary / count if count else 0
    average_age = total_age / count if count else 0

    return average_salary, average_age
