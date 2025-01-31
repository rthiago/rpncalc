import inspect
import math
import operator
import random
import re
import socket

import state


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
    '%': operator.mod,
    '++': lambda a: a + 1,
    '--': lambda a: a - 1,
    '|': lambda a, b: operator.or_(int(a), int(b)),
    '&': lambda a, b: operator.and_(int(a), int(b)),
    '^': lambda a, b: operator.xor(int(a), int(b)),
    '~': lambda a: operator.inv(int(a)),
    '>>': lambda a, b: operator.rshift(int(a), int(b)),
    '<<': lambda a, b: operator.lshift(int(a), int(b)),
    'hex': lambda: state.set_mode('hex'),
    'dec': lambda: state.set_mode('dec'),
    'oct': lambda: state.set_mode('oct'),
    'bin': lambda: state.set_mode('bin'),
    'hnl': lambda a: socket.htonl(int(a)),
    'hns': lambda a: socket.htons(int(a)),
    'nhl': lambda a: socket.ntohl(int(a)),
    'nhs': lambda a: socket.ntohs(int(a)),
    '&&': lambda a, b: a and b,
    '||': lambda a, b: a or b,
    '^^': lambda a, b: int(a) ^ int(b),
    '!': lambda a: float(not a),
    '!=': lambda a, b: float(a != b),
    '<': lambda a, b: float(a < b),
    '<=': lambda a, b: float(a <= b),
    '==': lambda a, b: float(a == b),
    '>': lambda a, b: float(a > b),
    '>=': lambda a, b: float(a >= b),
    'clv': lambda: state.clear_variables(),
}


STACK_FUNCTIONS = {
    'max': lambda a: a + [max(a)],
    'min': lambda a: a + [min(a)],
    'clr': lambda a: [],
    'e': lambda a: a + [math.e],
    'pi': lambda a: a + [math.pi],
    'rand': lambda a: a + [random.random()],
    'dup': lambda a: a + [a[-1]],
    'drop': lambda a: a[:-1],
    'depth': lambda a: a + [float(len(a))],
    'swap': lambda a: a[:-2] + [a[-1]] + [a[-2]],
    'cla': lambda a: clear_all(a),
}


def handle(expression, stack):
    if expression in STACK_FUNCTIONS:
        operation = STACK_FUNCTIONS[expression]
        return operation(stack)

    if is_variable_assignment(expression):
        state.assign_variable(expression.replace('=', ''), stack.pop())
        return stack

    operation = OPERATIONS[expression]

    arg_count = len(inspect.getfullargspec(operation).args)

    if arg_count == 2:
        stack.append(operation(stack.pop(-2), stack.pop()))

    elif arg_count == 1:
        stack.append(operation(stack.pop()))

    else:
        operation()

    return stack


def can_handle(expression):
    return is_variable_assignment(expression) or is_function(expression)


def is_function(expression):
    return expression in OPERATIONS or expression in STACK_FUNCTIONS


def is_variable_assignment(expression):
    if re.search('^[a-zA-Z_]+=', expression):
        if is_function(expression.replace('=', '')):
            raise ValueError(
                'Variable cannot have same name as an internal function.')

        return True

    return False


def clear_all(stack):
    stack = []
    state.clear_variables()

    return stack
