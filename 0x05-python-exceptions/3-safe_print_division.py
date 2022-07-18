#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        work = a / b
    except:
        work = None
    finally:
        print("Inside result: {}".format(work))
    return (work)
