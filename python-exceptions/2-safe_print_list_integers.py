#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    funciona = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end=" ")
            funciona += 1
        except (ValueError, TypeError, IndexError):
            continue
    print()
    return funciona
