#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        work = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        work = None

    return (work)
