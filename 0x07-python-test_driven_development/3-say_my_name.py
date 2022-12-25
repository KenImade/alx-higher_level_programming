#!/usr/bin/python3
"""
This module defines the `say_my_name`

The function prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=''):
    """
    prints My name is <first name> <last name>

    Args:
        first_name: a string
        last_name: a string

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string

    Returns:
        Nothing
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    else:
        first_name = first_name.title()

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    else:
        last_name = last_name.title()

    print('My name is {} {}'.format(first_name, last_name), end='')
