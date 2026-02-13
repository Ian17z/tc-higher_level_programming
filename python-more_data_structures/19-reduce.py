#!/usr/bin/python3
from functools import reduce
def media_age_salary(data):
    valores = [data.get("age", 0), data.get("salary", 0)]
    media = reduce(lambda x, y: x + y, valores) / len(valores)
    print(media)
