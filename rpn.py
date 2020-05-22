#!/usr/bin/python

from pathlib import Path
import re
import readline
import sys

import colors
import operations
import state


def calculate(expressions, stack):
    expressions = evaluate_macros(expressions)

    for expression in expressions.split():
        try:
            if operations.can_handle(expression):
                stack = operations.handle(expression, stack)

            elif is_number(expression):
                append_number(expression, stack)

            elif expression in state.get_variables():
                value = state.get_variable_value(expression)
                append_number(value, stack)

            else:
                print("Don't know what to do with " + expression,
                      file=sys.stderr)

        except IndexError:
            print('Stack too shallow. Push more values.', file=sys.stderr)

        except (OverflowError, ValueError) as err:
            print('Invalid value: ' + str(err), file=sys.stderr)

        except ZeroDivisionError:
            print("You can't divide by zero.", file=sys.stderr)

    return stack


def evaluate_macros(expressions):
    expressions = store_new_macros(expressions)
    expressions = execute_macros(expressions)

    return expressions


def store_new_macros(expressions):
    """Find all new macros and store them.
    """

    regex = r'(^|\s)macro ([a-z]+) (.*?)(;|\n|$)'
    for macro in re.findall(regex, expressions, re.MULTILINE):
        if operations.is_function(macro[1]):
            print('Macro cannot have same name as an internal function.',
                  file=sys.stderr)

        state.assign_macro(macro[1], macro[2])

    expressions = re.sub(r'\bmacro.*?(;|\n|$)', ' ', expressions, re.MULTILINE)

    return expressions


def execute_macros(expressions):
    """Replaces macros to be executed with its actual commands.
    """

    for name, macro in state.get_macros().items():
        regex = r'\b{}(\s|$)'.format(name)
        expressions = re.sub(regex, ' ' + macro + ' ', expressions)

    return expressions


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

            if user_input == 'macros':
                print(state.get_macros())

            else:
                stack = calculate(user_input, stack)

    except (EOFError, KeyboardInterrupt):
        pass


def parse_rc():
    try:
        with open(str(Path.home()) + '/.rpnrc') as rc:
            return calculate(rc.read(), [])

    except FileNotFoundError:
        return []


def format_prompt(stack):
    prompt = colors.LIGHTBLACK + state.get_mode()
    prompt += colors.RESET + format_variables()

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
