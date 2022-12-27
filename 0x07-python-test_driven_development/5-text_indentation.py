#!/usr/bin/python3
"""
This module defines `text_indentation`

The function prints text and new line when it encounters
'.', '?', or ':'
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these
    characters: '.', '?', and ':'

    Args:
        text: string

    Raises:
        TypeError: text must be a string

    Returns:
        Nothing
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    arr = list(text)

    for char in arr:
        if char == '.' or char == '?' or char == ':':
            print('{}'.format(char), end='')
            print('\n\n')
        else:
            print('{}'.format(char), end='')
