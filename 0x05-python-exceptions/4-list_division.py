#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newl = []

    for i in range(list_length):
        try:
            work = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            work = 0
        except TypeError:
            print("wrong type")
            work = 0
        except IndexError:
            print("out of range")
            work = 0
        finally:
            newl.append(work)

    return (newl)
