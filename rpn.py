#!/usr/bin/python

import operator
import sys


OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.truediv,
    '*': operator.mul,
}


def calculate(expressions, stack):
    for expression in expressions:
        if is_number(expression):
            stack.append(float(expression))
        else:
            operation = OPERATIONS[expression]
            stack.append(operation(stack.pop(-2), stack.pop()))

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
    print(calculate(expressions, []).pop())


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
