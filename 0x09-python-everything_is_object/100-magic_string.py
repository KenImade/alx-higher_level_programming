#!/usr/bin/python3


def call_counter(func):
    def helper():
        helper.call += 1
        return func()
    helper.call = 0

    return helper


@call_counter
def magic_string():
    return 'BestSchool, ' * (magic_string.calls - 1) + 'BestSchool'
