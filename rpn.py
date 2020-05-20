#!/usr/bin/python

import re
import readline
import sys

import operations
import state


def calculate(expressions, stack):
    for expression in expressions:
        if operations.can_handle(expression):
            try:
                stack = operations.handle(expression, stack)

            except IndexError:
                print('Stack too shallow. Push more values.', file=sys.stderr)

            except (OverflowError, ValueError):
                print('Invalid value for ' + expression + '.', file=sys.stderr)

            except ZeroDivisionError:
                print("You can't divide by zero.", file=sys.stderr)

        elif is_number(expression):
            base = guess_base(expression)
            if base == 10:
                stack.append(float(expression))
            else:
                stack.append(int(expression, base))

        else:
            print("Don't know what to do...", file=sys.stderr)

    return stack


def is_number(value):
    return (re.search(r'^[-+]?[0-9]+\.?[0-9]*$', value)
            or re.search('^(0b)?[01]+$', value)
            or re.search('^(0x)?[0-9a-f]+$', value)
            or re.search('^(0o)?[0-7]+$', value))


def guess_base(value):
    if re.search('^0b', value):
        return 2

    if re.search('^0o', value):
        return 8

    if re.search('^0x', value):
        return 16

    return 10


def print_help():
    print('help')


def one_shot(expressions):
    result = calculate(expressions, [])
    if len(result) > 0:
        print(format_output(result))


def interactive():
    stack = []

    try:
        while True:
            prompt = state.get_mode() + ' ' + format_output(stack) + ' > '
            user_input = input(prompt.lstrip().replace('  ', ' '))

            if user_input == 'exit':
                break

            if user_input == 'help':
                print_help()
            else:
                stack = calculate(user_input.split(), stack)

    except (EOFError, KeyboardInterrupt):
        print()  # Line break.

    print('Bye')


def format_output(stack):
    if state.get_mode() == 'dec':
        return ' '.join(map(format_number, stack))

    tmp = []

    for value in stack:
        tmp.append(state.convert(value))

    return ' '.join(map(format_number, tmp))


def format_number(value):
    return re.sub(r'\.0+$', '', str(value))


def main():
    sys.argv.pop(0)

    if not sys.stdin.isatty():
        one_shot(sys.stdin.read().split())
        return

    if len(sys.argv) == 0:
        interactive()
        return

    if sys.argv[0] == '--help':
        print_help()
    else:
        one_shot(sys.argv)


if __name__ == '__main__':
    main()
