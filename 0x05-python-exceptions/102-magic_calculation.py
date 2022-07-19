#!/usr/bin/python3
def magic_calculation(a, b):
    work = 0

    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception("Too far")
            else:
                work += (a ** b) / i
            except:
                work = b + a
                break

    return (work)
