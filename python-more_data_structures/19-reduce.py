#!/usr/bin/python3
from functools import reduce
#!/usr/bin/python3
from functools import reduce
def calc_average(data):
    values = list(data.values())
    total = len(values)
    total_salary = reduce(lambda acc, x: acc + x["salary"], values, 0)
    total_age = reduce(lambda acc, x: acc + x["age"], values, 0)
    avg_salary = total_salary / total
    avg_age = total_age / total
    print(
        f"The average salary is R${avg_salary:.2f} "
        f"with an average age of {avg_age:.2f}"
    )
