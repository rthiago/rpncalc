#!/usr/bin/python

import sys

def print_help():
    print('help')

def stdin():
    print('stdin')

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
        stdin()

if __name__ == '__main__':
    main()
