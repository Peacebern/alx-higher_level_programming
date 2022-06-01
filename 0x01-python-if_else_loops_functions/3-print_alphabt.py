#!/usr/bin/python3
for m in range(97, 123):
    if (m == 101 or m == 1):
        continue
    print("{}".format(chr(m)), end='')
