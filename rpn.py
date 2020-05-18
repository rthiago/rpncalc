#!/usr/bin/python

import operator
import sys


operations = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul,
}


def calculate(expressions, stack):
    for expression in expressions:
        if expression.isnumeric():
            stack.append(float(expression))
        else:
            operation = operations[expression]
            stack.append(operation(stack.pop(-2), stack.pop()))

    return stack


def print_help():
    print('help')


def one_shot(expressions):
    print(calculate(expressions, []).pop())


def interactive():
    stack = []

    while True:
        stack = calculate(input(' '.join(map(str, stack)) + ' > ').split(), stack)


def main():
    sys.argv.pop(0)

    if not len(sys.argv):
        interactive()
        return

    if sys.argv[0] == '--help':
        print_help()
    else:
        one_shot(sys.argv)


if __name__ == '__main__':
    main()
