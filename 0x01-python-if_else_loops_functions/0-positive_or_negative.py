#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"is positive\n")
if number == 0:
    print(f"is zero\n")
if number < 0:
    print(f"is negative\n")
