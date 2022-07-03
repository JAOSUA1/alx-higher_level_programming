#!/usr/bin/python3
def max_integer(my_list=[]):
    ful_len = len(my_list)

    if ful_len == 0:
        return (None)
    num_max = my_list[0]

    for i in range(1, ful_len):
        if my_list[i] > num_max:
            num_max = my_list[i]

    return (num_max)
