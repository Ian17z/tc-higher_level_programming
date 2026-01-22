#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in range(x):
        try:
            valor = my_list[i]
            if type(valor) is int:
                print("{:d}".format(valor), end="")
                num += 1
        except IndexError:
            break
    print()
    return num
