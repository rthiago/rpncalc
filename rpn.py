#!/usr/bin/python

import operator
import sys


operations = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul,
}


def calculate(expressions):
    stack = []

    for expression in expressions:
        if expression.isnumeric():
            stack.append(float(expression))
        else:
            operation = operations[expression]
            stack.append(operation(stack.pop(-2), stack.pop()))

    return stack.pop()


def print_help():
    print('help')


def stdin(expressions):
    print(calculate(expressions))


def interactive():
    print('interactive')


def main():
    sys.argv.pop(0)

    if not len(sys.argv):
        interactive()
        return

    if sys.argv[0] == '--help':
        print_help()
    else:
        stdin(sys.argv)


if __name__ == '__main__':
    main()
