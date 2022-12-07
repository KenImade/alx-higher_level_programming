#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key == "":
        return a_dictionary

    for k, v in a_dictionary.items():
        if k == key:
            del a_dictionary[key]

    return a_dictionary
