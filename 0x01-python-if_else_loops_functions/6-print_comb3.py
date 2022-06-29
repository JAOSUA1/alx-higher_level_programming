#!/usr/bin/python3
for no in range(0, 90):
    if no % 10 > no / 10:
        if no != 89:
            print("{:02d}, ".format(no), end='')
        else:
            print("{:02d}".format(no))
