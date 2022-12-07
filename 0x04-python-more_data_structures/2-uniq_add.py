#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_numbers = set(my_list)
    
    sum = 0
    for num in uniq_numbers:
        sum = num + sum

    return sum
