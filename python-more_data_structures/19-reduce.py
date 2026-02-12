#!/usr/bin/python3
from functools import reduce
from functools import reduce
def calc_average(a_dictionary):
    values = a_dictionary.values()
    n = len(a_dictionary)
    total_age = reduce(lambda acc, emp: acc + emp["age"], values, 0)
    total_salary = reduce(lambda acc, emp: acc + emp["salary"], values, 0)
    avg_age = total_age / n
    avg_salary = total_salary / n
    print(f"The average salary is R${avg_salary:.2f} with an average age of {avg_age:.2f}")
