#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return 0
    weighted_sum = sum(list(map(lambda x: x[0] * x[1], my_list)))
    weights = sum(list(map(lambda x: x[1], my_list)))
    weighted_average = weighted_sum / weights
    return weighted_average
