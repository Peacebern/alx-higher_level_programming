#!/usr/bin/python3

if __name__ == '__main__':
    from calculator_1 import add, sub, div, mul

    import sys

    opert = {"+": add, "-": sub, "*": mul, "/": div}

    if len(sys.argv) -1 != 3:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
        # create an array of various operators

       # opert = {"+": add, "-": sub, "*": mul, "/": div}

    elif sys.argv[2] not in list(opert.keys()):
        print("unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)

    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print("{} {} {} = {}".format(a, sys.argv[2], b, opert[sys.argv[2]](a, b)))
