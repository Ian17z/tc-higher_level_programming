#!/usr/bin/python3
def search_replace(my_list, search, replace):
    novalista = []
    for i in my_list:
        if i == search:
            novalista.append(replace)
        else:
            novalista.append(i)
    return novalista
