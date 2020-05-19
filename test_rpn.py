import rpn


def test_basic_operations():
    results = rpn.calculate('6 7 + 5 * 4 + 3 *'.split(), [])
    assert results == [207]

    results = rpn.calculate('12 34 + 56 + 78 - 90 + 12 -'.split(), [])
    assert results == [102]

    results = rpn.calculate('12 34 * 56 78 * + 90 12 * -'.split(), [])
    assert results == [3696]


def test_math_functions():
    results = rpn.calculate('2 3 pow'.split(), [])
    assert results == [8]

    results = rpn.calculate('4 fact'.split(), [])
    assert results == [24]

    results = rpn.calculate('9 sqrt'.split(), [])
    assert results == [3]

    results = rpn.calculate('10 ln'.split(), [])
    assert results == [2.3978952727983707]

    results = rpn.calculate('10 log'.split(), [])
    assert results == [1]


def test_utilities():
    results = rpn.calculate('9.1 ceil'.split(), [])
    assert results == [10]

    results = rpn.calculate('9.1 floor'.split(), [])
    assert results == [9]

    results = rpn.calculate('9.458801 2 round'.split(), [])
    assert results == [9.46]

    results = rpn.calculate('9.458801 ip'.split(), [])
    assert results == [9]

    results = rpn.calculate('9.458801 fp'.split(), [])
    assert round(results.pop(), 6) == 0.458801

    results = rpn.calculate('-1 sign 1 sign'.split(), [])
    assert results == [1, -1]

    results = rpn.calculate('-1 abs 1 abs'.split(), [])
    assert results == [1, 1]

    results = rpn.calculate('14 11 10 20 12 max'.split(), [])
    assert results.pop() == 20

    results = rpn.calculate('14 11 10 20 12 min'.split(), [])
    assert results.pop() == 10


def test_trigonometric_functions():
    results = rpn.calculate('0.5 acos'.split(), [])
    assert round(results.pop(), 8) == 1.04719755

    results = rpn.calculate('1 asin'.split(), [])
    assert round(results.pop(), 8) == 1.57079633

    results = rpn.calculate('1 atan'.split(), [])
    assert round(results.pop(), 8) == 0.78539816

    results = rpn.calculate('1 cos'.split(), [])
    assert round(results.pop(), 8) == 0.54030231

    results = rpn.calculate('1 cosh'.split(), [])
    assert round(results.pop(), 8) == 1.54308063

    results = rpn.calculate('1 sin'.split(), [])
    assert round(results.pop(), 8) == 0.84147098

    results = rpn.calculate('1 sinh'.split(), [])
    assert round(results.pop(), 8) == 1.17520119

    results = rpn.calculate('1 tanh'.split(), [])
    assert round(results.pop(), 8) == 0.76159416


def test_commands():
    results = rpn.calculate('1 2 3 clr 4 5 6 +'.split(), [])
    assert results == [4, 11]

    results = rpn.calculate('1 e 3'.split(), [])
    assert results == [1, 2.718281828459045, 3]

    results = rpn.calculate('1 2 pi'.split(), [])
    assert results == [1, 2, 3.141592653589793]

    results = rpn.calculate('rand'.split(), [])
    assert float(results.pop()) < 1

    results = rpn.calculate('1 2 3 dup'.split(), [])
    assert results == [1, 2, 3, 3]

    results = rpn.calculate('1 2 3 drop'.split(), [])
    assert results == [1, 2]

    results = rpn.calculate('3 4 5 12 depth'.split(), [])
    assert results == [3, 4, 5, 12, 4]

    results = rpn.calculate('3 4 5 12 swap'.split(), [])
    assert results == [3, 4, 12, 5]
