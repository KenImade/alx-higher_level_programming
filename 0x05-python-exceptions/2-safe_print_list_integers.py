#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for index in range(x):
        try:
            number = int(my_list[index])
            print("{:d}".format(number), end="")
            count += 1
        except IndexError:
            raise IndexError
        except TypeError:
            continue
        except ValueError:
            continue
    print()
    return count
