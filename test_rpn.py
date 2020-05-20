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


def test_operators():
    results = rpn.calculate('5 2 %'.split(), [])
    assert results == [1]

    results = rpn.calculate('5 ++'.split(), [])
    assert results == [6]

    results = rpn.calculate('333 --'.split(), [])
    assert results == [332]


def test_bitwise():
    results = rpn.calculate('1 2 |'.split(), [])
    assert results == [3]

    results = rpn.calculate('12 55 &'.split(), [])
    assert results == [4]

    results = rpn.calculate('2 9 ^'.split(), [])
    assert results == [11]

    results = rpn.calculate('4 ~'.split(), [])
    assert results == [-5]

    results = rpn.calculate('4 1 >>'.split(), [])
    assert results == [2]

    results = rpn.calculate('4 2 <<'.split(), [])
    assert results == [16]


def test_modes():
    results = rpn.calculate('hex 0x6 0x7 + 0x5 * 0x4 + 3 * 0xf +'.split(), [])
    assert results == [0xde]

    results = rpn.calculate('oct 0o6 0o7 + 0o5 * 0o4 + 3 * 0o17 +'.split(), [])
    assert results == [0o336]

    results = rpn.calculate('bin 0b110 0b111 + 0b101 * 0b100 + 0b11 * 0b1111 +'.split(), [])
    assert results == [0b11011110]

    results = rpn.calculate('bin 0b110 hex 0x7 + oct 0o5 * bin 0b100 + dec 3 * 15 +'.split(), [])
    assert results == [222]

    results = rpn.calculate('bin 0xaa55 2 | 1 ~ &'.split(), [])
    assert results == [0b1010101001010110]


def test_networking():
    results = rpn.calculate('3232235521 hnl'.split(), [])
    assert results == [16820416]

    results = rpn.calculate('16820416 nhl'.split(), [])
    assert results == [3232235521]

    results = rpn.calculate('4096 hns'.split(), [])
    assert results == [16]

    results = rpn.calculate('16 nhs'.split(), [])
    assert results == [4096]

def test_errors(capsys):
    results = rpn.calculate('-1 hnl'.split(), [])
    captured = capsys.readouterr()
    assert len(captured.err) > 0
    assert results == []
