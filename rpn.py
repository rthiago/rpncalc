#!/usr/bin/python

import sys

def print_help():
    print('help')

def stdin(expressions):
    stack = []

    for expression in expressions:
        if expression.isnumeric():
            stack.append(expression)
        else:
            stack.append(eval(stack.pop(-2) + expression + stack.pop(-1)))

    print(stack)

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
