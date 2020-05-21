class State:
    mode = 'dec'

    variables = {}


def set_mode(mode):
    State.mode = mode


def get_mode():
    return State.mode


def get_base():
    bases = {
        'bin': 2,
        'oct': 8,
        'dec': 10,
        'hex': 16,
    }

    return bases[get_mode()]


def convert(value):
    converters = {
        'bin': bin,
        'oct': oct,
        'dec': float,
        'hex': hex,
    }

    return converters[get_mode()](int(value))


def assign_variable(name, value):
    State.variables[name] = value


def get_variables():
    return State.variables
