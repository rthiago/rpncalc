class State:
    mode = 'dec'

    variables = {}

    macros = {}


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

    if get_mode() != 'dec':
        value = int(value)

    return converters[get_mode()](value)


def assign_variable(name, value):
    State.variables[name] = value


def get_variables():
    return State.variables


def get_variable_value(variable):
    return State.variables[variable]


def clear_variables():
    State.variables.clear()


def assign_macro(name, value):
    State.macros[name] = value.strip()


def get_macros():
    return State.macros
