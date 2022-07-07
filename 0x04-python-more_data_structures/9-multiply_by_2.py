#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_ones = a_dictionary.copy()
    list_keys = list(new_ones.keys())

    for i in list_keys:
        new_ones[i] = new_ones[i] * 2
    return (new_ones)
