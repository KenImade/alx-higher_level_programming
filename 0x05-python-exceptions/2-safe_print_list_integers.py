#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while (i < x):
        try:
            number = int(my_list[i])
            print("{:d}".format(number), end="")
        except ValueError:
            continue
        except IndexError:
            break
        else:
            i += 1
    return i
