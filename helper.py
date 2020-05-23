COMMANDS = {
    'Mathematic': {
        '+': 'Sum',
        '-': 'Difference',
        '/': 'Division',
        '*': 'Multiplication',
        'pow': 'Power (x**y)',
        'sqrt': 'Square root',
        '%': 'Modulus',
        '++': 'Increment by 1',
        '--': 'Decrement by 1',
        'ceil': 'Round up',
        'floor': 'Round down',
        'round': 'Round numbers. Takes 2 arguments: "5.2343 2 round" results in 5.23',
        'ip': 'Push the integer part',
        'fp': 'Push the float part',
        'sign': 'Invert sign',
        'abs': 'Absolute value',
        'fact': 'Factorial',
    },
    'Power and logaritimic': {
        'exp': 'Exponentiation (e**n)',
        'ln': 'Natural logarithm of 1+x (base e)',
        'log': 'Natural logarithm of x',
    },
    'Trigonometric and hyperbolic': {
        'acos': 'Arc cosine',
        'asin': 'Arc sine',
        'atan': 'Arc tangent',
        'cos': 'Cosine',
        'cosh': 'Hyperbolic cosine',
        'sin': 'Sine',
        'sinh': 'Hyperbolic sine',
        'tanh': 'Hyperbolic tangent',
    },
    'Bitwise operators': {
        '|': 'Or',
        '&': 'And',
        '^': 'Xor',
        '~': 'Not',
        '>>': 'Right shift',
        '<<': 'Left shift',
    },
    'Number modes': {
        'bin': 'Binary mode',
        'dec': 'Decimal mode',
        'hex': 'Hexadecimal mode',
        'oct': 'Octal mode',
    },
    'Networking functions': {
        'hnl': 'Host to network long',
        'hns': 'Host to network short',
        'nhl': 'Network to host long',
        'nhs': 'Network to host short',
    },
    'Logical operators': {
        '&&': 'And',
        '||': 'Or',
        '^^': 'Xor',
        '!': 'Not',
        '!=': 'Not equals',
        '<': 'Less than',
        '<=': 'Less than or equal to',
        '==': 'Equal to',
        '>': 'Greater than',
        '>=': 'Greater than or equal to',
    },
    'Stack': {
        'max': 'Push the higher value in stack',
        'min': 'Push the lower value in stack',
        'e': "Push Euler's constant",
        'pi': 'Push Pi',
        'rand': 'Push a random number',
        'dup': 'Duplicates the top value',
        'drop': 'Drops the top value',
        'depth': 'Push the stack height',
        'swap': 'Swap top two stack values',
    },
    'Other': {
        'cla': 'Clear all variables and stack values',
        'clr': 'Clear all stack values',
        'clv': 'Clear all variables',
        'macro': 'Create a macro. Must end with new line, EOF or semicolon: macro bar 1 2 3 + +',
        'macros': 'List current macros',
        'foo=': 'Assign variable',
        'exit': 'Exit interactive mode',
    }
}


CLI = {
    'Usage': {
        'python rpn.py': 'Enter interactive mode',
        'python rpn.py [Expressions]': 'Evaluate expressions',
    },
    'Rc file': {
        'Put a .rpnrc file in your home directory to preload expressions, stack or variables': '',
    },
    'Options': {
        '--help': 'This help',
        '--commands': 'Full list of commands',
    },
    'Examples': {
        'python rpn.py 10 20 30 + /': '',
        'python rpn.py 64 bin': '',
        'cat foobar.txt | python rpn.py': '',
    }
}


def commands():
    print_dict(COMMANDS.items(), 4, 10)


def cli():
    print_dict(CLI.items(), 1, 30)


def print_dict(items, spaces, just):
    for key, value in items:
        if isinstance(value, dict):
            print('{}{}'.format(' ' * spaces, key))
            print_dict(value.items(), spaces + 3, just)
            print()
        else:
            print('{}{}{}'.format(' ' * spaces, key.ljust(just), value))
