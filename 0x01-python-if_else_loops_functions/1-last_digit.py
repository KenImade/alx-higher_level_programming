#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = str(number)[-1]
if number > 0:
    last_digit = int(temp)
else:
    last_digit = -1 * int(temp)
message = "Last digit of"
if last_digit > 5:
    print(f"{message} {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{message} {number} is {last_digit} and is 0")
elif last_digit < 6 and last_digit != 0:
    print(f"{message} {number} is {last_digit} and is less than 6 and not 0")
