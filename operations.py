import math
import inspect
import operator


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
    'max': lambda a: a + [max(a)],
    'min': lambda a: a + [min(a)],
    'clr': lambda a: [],
    'e': lambda a: a + [math.e],
    'pi': lambda a: a + [math.pi],
}


STACK_FUNCTIONS = [
    'min',
    'max',
    'clr',
    'e',
    'pi',
]


def handle(expression, stack):
    operation = OPERATIONS[expression]

    if expression in STACK_FUNCTIONS:
        # Whole stack functions.
        stack = operation(stack)

    elif len(inspect.getfullargspec(operation).args) == 2:
        # Two argument functions
        stack.append(operation(stack.pop(-2), stack.pop()))

    else:
        # Single argument functions
        stack.append(operation(stack.pop()))

    return stack

def can_handle(expression):
    return expression in OPERATIONS
