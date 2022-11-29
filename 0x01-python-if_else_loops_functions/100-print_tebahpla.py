#!/usr/bin/python3

i = 0

for c in range(122, 96, -1):
    if i % 2 != 0:
        c = c - 32
    i += 1
    print("{:c}".format(c), end="")
