#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    chck = []

    for i range(len(my_list)):
        if my_list[i] % 2 == 0:
            chck.append(True)
        else:
            chck.append(False)
    return (chck)
