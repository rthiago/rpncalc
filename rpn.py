#!/usr/bin/python

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
        elif is_number(expression):
            if state.get_mode() == 'dec':
                stack.append(float(expression))
            else:
                stack.append(int(expression, state.get_base()))
        else:
            print("Don't know what to do...", file=sys.stderr)

    return stack


def is_number(val):
    try:
        if state.get_mode() == 'dec':
            float(val)
        else:
            int(val, state.get_base())

        return True
    except ValueError:
        return False


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

            stack = calculate(user_input.split(), stack)

    except (EOFError, KeyboardInterrupt):
        print()  # Line break.

    print('Bye')


def format_output(stack):
    if state.get_mode() == 'dec':
        return ' '.join(map(str, stack))

    tmp = []

    for value in stack:
        tmp.append(state.convert(value))

    return ' '.join(map(str, tmp))


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
