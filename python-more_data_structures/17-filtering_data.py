#!/usr/bin/python3
def filtering_data(a_dictionary):
    return list(map(lambda emp: emp["name"],
                    filter(lambda emp: emp["salary"] > 10000, a_dictionary)))
