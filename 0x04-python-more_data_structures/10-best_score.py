#!/usr/bin/python3 

def best_score(a_dictionary):
    max = None

    for k, v in a_dictionary.items():
        max = max(a_dictionary[k], max)

    return max
