#!/usr/bin/python

import inspect
import math
import operator
import sys


OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul,
    'pow': math.pow,
    'sqrt': math.sqrt,
    'acos': math.acos,
    'asin': math.asin,
    'atan': math.atan,
    'cos': math.cos,
    'cosh': math.cosh,
    'sin': math.sin,
    'sinh': math.sinh,
    'tanh': math.tanh,
    'ceil': math.ceil,
    'floor': math.floor,
    'round': lambda a, b: round(a, int(b)),
    'ip': lambda a: a // 1,
    'fp': lambda a: a % 1,
    'sign': lambda a: a * -1,
    'abs': math.fabs,
    'fact': math.factorial,
    'ln': math.log1p,
    'log': math.log10,
    'exp': math.exp,
}


def calculate(expressions, stack):
    for expression in expressions:
        if is_number(expression):
            stack.append(float(expression))
        else:
            operation = OPERATIONS[expression]
            try:
                if len(inspect.getfullargspec(operation).args) == 2:
                    # Two argument functions
                    stack.append(operation(stack.pop(-2), stack.pop()))
                else:
                    # Single argument functions
                    stack.append(operation(stack.pop()))
            except IndexError:
                print('Stack too shallow. Push more values.')

    return stack


def is_number(val):
    try:
        float(val)
        return True
    except ValueError:
        return False


def print_help():
    print('help')


def one_shot(expressions):
    result = calculate(expressions, [])
    if len(result) > 0:
        print(result.pop())


def interactive():
    stack = []

    try:
        while True:
            prompt = ' '.join(map(str, stack)) + ' > '
            user_input = input(prompt.lstrip())

            if user_input == 'exit':
                break
            elif user_input == 'clr':
                stack = []
            else:
                stack = calculate(user_input.split(), stack)
    except (EOFError, KeyboardInterrupt):
        print()  # Line break.

    print('Bye')


def main():
    sys.argv.pop(0)

    if len(sys.argv) == 0:
        interactive()
        return

    if sys.argv[0] == '--help':
        print_help()
    else:
        one_shot(sys.argv)


if __name__ == '__main__':
    main()
