#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"is positive\n")
elif number == 0:
    print(f"is zero\n")
elif number < 0:
    print(f"is negative\n")
