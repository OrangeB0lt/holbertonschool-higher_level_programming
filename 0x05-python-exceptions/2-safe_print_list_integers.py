#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    fin = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            fin += 1
        except (TypeError, ValueError):
            idx += 1
            continue
    print("")
    return fin
