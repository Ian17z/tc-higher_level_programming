#!/usr/bin/python3
from functools import reduce
def calc_average(a_dictionary):
    valores = a_dictionary.valores()
    n = len(a_dictionary)
    totalidade = reduce(lambda acc, emp: acc + emp["age"], valores, 0)
    totalsalario = reduce(lambda acc, emp: acc + emp["salary"], valores, 0)
    mediaidade = totalidade / n
    averagesalario = totalsalario / n
