#!/usr/bin/python

import operations
import sys


def calculate(expressions, stack):
    for expression in expressions:
        if is_number(expression):
            stack.append(float(expression))
        elif operations.can_handle(expression):
            try:
                stack = operations.handle(expression, stack)
            except IndexError:
                print('Stack too shallow. Push more values.')
        else:
            print("Don't know what to do...")

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
