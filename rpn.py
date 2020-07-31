#!/usr/bin/python

from pathlib import Path
import re
import readline
import sys

import colors
import operations
import state


def calculate(expressions, stack):
    for expression in expressions:
        try:
            if operations.can_handle(expression):
                stack = operations.handle(expression, stack)

            elif is_number(expression):
                append_number(expression, stack)

            elif expression in state.get_variables():
                value = state.get_variable_value(expression)
                append_number(value, stack)

            else:
                print("Don't know what to do...", file=sys.stderr)

        except IndexError:
            print('Stack too shallow. Push more values.', file=sys.stderr)

        except (OverflowError, ValueError) as err:
            print('Invalid value: ' + str(err), file=sys.stderr)

        except ZeroDivisionError:
            print("You can't divide by zero.", file=sys.stderr)

    return stack


def is_number(value):
    return (re.search(r'^[-+]?[0-9]+\.?[0-9]*$', value)
            or re.search('^(0b)?[01]+$', value)
            or re.search('^(0x)?[0-9a-f]+$', value)
            or re.search('^(0o)?[0-7]+$', value))


def append_number(value, stack):
    base = guess_base(str(value))

    if base == 10:
        stack.append(float(value))

    else:
        stack.append(int(value, base))

    return stack


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
    stack = parse_rc()
    result = calculate(expressions, stack)

    if len(result) > 0:
        print(format_output(result))


def interactive():
    stack = parse_rc()

    try:
        while True:
            user_input = input(format_prompt(stack))

            if user_input == 'exit':
                break

            if user_input == 'help':
                print_help()

            else:
                stack = calculate(user_input.split(), stack)

    except (EOFError, KeyboardInterrupt):
        pass


def parse_rc():
    try:
        with open(str(Path.home()) + '/.rpnrc') as rc:
            return calculate(rc.read().split(), [])

    except FileNotFoundError:
        return []


def format_prompt(stack):
    prompt = colors.LIGHTBLACK + state.get_mode()
    prompt +=  colors.RESET + format_variables()

    if len(stack) > 0:
        prompt += ' ' + colors.LIGHTWHITE + format_output(stack)

    prompt += colors.GREEN + ' > ' + colors.RESET

    return prompt


def format_variables():
    variables = state.get_variables()
    if len(variables) == 0:
        return ''

    items = []
    for key, value in variables.items():
        items.append(key + '=' + format_number(state.convert(value)))

    return ' [ ' + ' '.join(items) + ' ]'


def format_output(stack):
    items = []
    for value in stack:
        items.append(state.convert(value))

    return ' '.join(map(format_number, items))


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
