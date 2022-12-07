#!/usr/bin/python3 

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return "None"
    else:
        max = 0
        name = ""
        for k, v in a_dictionary.items():
            if a_dictionary[k] > max:
                max = a_dictionary[k]
                name = k
        return name
