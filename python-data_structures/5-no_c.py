#!/usr/bin/python3
def no_c(my_string):
    nova = ""
    for idx in my_string:
        if idx != 'c' and idx != 'C':
            nova += idx
    return nova
