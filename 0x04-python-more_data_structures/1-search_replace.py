#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if search not in my_list:
        return my_list

    new_list = my_list.copy()

    for i, v in enumerate(new_list):
        if v == search:
            new_list[i] = replace

    return new_list
