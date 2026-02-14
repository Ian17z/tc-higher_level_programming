#!/usr/bin/python3
from functools import reduce
def calc_average(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return
    age_list = a_dictionary.get("age", [])
    salary_list = a_dictionary.get("salary", [])
    def average(lst):
        return reduce(lambda acc, x: acc + x, lst, 0) / len(lst) if lst else 0
    age_avg, salary_avg = average(age_list), average(salary_list)
    print(f"Average age: {age_avg}")
    print(f"Average salary: {salary_avg}")
