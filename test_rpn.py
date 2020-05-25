import rpn


def test_basic_operations():
    results = rpn.calculate('6 7 + 5 * 4 + 3 *', [])
    assert results == [207]

    results = rpn.calculate('12 34 + 56 + 78 - 90 + 12 -', [])
    assert results == [102]

    results = rpn.calculate('12 34 * 56 78 * + 90 12 * -', [])
    assert results == [3696]


def test_math_functions():
    results = rpn.calculate('2 3 pow', [])
    assert results == [8]

    results = rpn.calculate('4 fact', [])
    assert results == [24]

    results = rpn.calculate('40 fact 1 +', [])
    assert results == [815915283247897734345611269596115894272000000001]

    results = rpn.calculate('9 sqrt', [])
    assert results == [3]

    results = rpn.calculate('10 ln', [])
    assert results == [2.3978952727983707]

    results = rpn.calculate('10 log', [])
    assert results == [1]


def test_utilities():
    results = rpn.calculate('9.1 ceil', [])
    assert results == [10]

    results = rpn.calculate('9.1 floor', [])
    assert results == [9]

    results = rpn.calculate('9.458801 2 round', [])
    assert results == [9.46]

    results = rpn.calculate('9.458801 ip', [])
    assert results == [9]

    results = rpn.calculate('9.458801 fp', [])
    assert round(results.pop(), 6) == 0.458801

    results = rpn.calculate('-1 sign 1 sign', [])
    assert results == [1, -1]

    results = rpn.calculate('-1 abs 1 abs', [])
    assert results == [1, 1]

    results = rpn.calculate('14 11 10 20 12 max', [])
    assert results.pop() == 20

    results = rpn.calculate('14 11 10 20 12 min', [])
    assert results.pop() == 10


def test_trigonometric_functions():
    results = rpn.calculate('0.5 acos', [])
    assert round(results.pop(), 8) == 1.04719755

    results = rpn.calculate('1 asin', [])
    assert round(results.pop(), 8) == 1.57079633

    results = rpn.calculate('1 atan', [])
    assert round(results.pop(), 8) == 0.78539816

    results = rpn.calculate('1 cos', [])
    assert round(results.pop(), 8) == 0.54030231

    results = rpn.calculate('1 cosh', [])
    assert round(results.pop(), 8) == 1.54308063

    results = rpn.calculate('1 sin', [])
    assert round(results.pop(), 8) == 0.84147098

    results = rpn.calculate('1 sinh', [])
    assert round(results.pop(), 8) == 1.17520119

    results = rpn.calculate('1 tanh', [])
    assert round(results.pop(), 8) == 0.76159416


def test_commands():
    results = rpn.calculate('1 2 3 clr 4 5 6 +', [])
    assert results == [4, 11]

    results = rpn.calculate('1 e 3', [])
    assert results == [1, 2.718281828459045, 3]

    results = rpn.calculate('1 2 pi', [])
    assert results == [1, 2, 3.141592653589793]

    results = rpn.calculate('rand', [])
    assert float(results.pop()) < 1

    results = rpn.calculate('1 2 3 dup', [])
    assert results == [1, 2, 3, 3]

    results = rpn.calculate('1 2 3 drop', [])
    assert results == [1, 2]

    results = rpn.calculate('3 4 5 12 depth', [])
    assert results == [3, 4, 5, 12, 4]

    results = rpn.calculate('3 4 5 12 swap', [])
    assert results == [3, 4, 12, 5]

    results = rpn.calculate('1 x= clv x', [])
    assert results == []

    results = rpn.calculate('1 2 x= cla x', [])
    assert results == []


def test_operators():
    results = rpn.calculate('5 2 %', [])
    assert results == [1]

    results = rpn.calculate('5 ++', [])
    assert results == [6]

    results = rpn.calculate('333 --', [])
    assert results == [332]


def test_bitwise():
    results = rpn.calculate('1 2 |', [])
    assert results == [3]

    results = rpn.calculate('12 55 &', [])
    assert results == [4]

    results = rpn.calculate('2 9 ^', [])
    assert results == [11]

    results = rpn.calculate('4 ~', [])
    assert results == [-5]

    results = rpn.calculate('4 1 >>', [])
    assert results == [2]

    results = rpn.calculate('4 2 <<', [])
    assert results == [16]


def test_modes():
    results = rpn.calculate('hex 0x6 0x7 + 0x5 * 0x4 + 3 * 0xf +', [])
    assert results == [0xde]

    results = rpn.calculate('oct 0o6 0o7 + 0o5 * 0o4 + 3 * 0o17 +', [])
    assert results == [0o336]

    results = rpn.calculate('bin 0b110 0b111 + 0b101 * 0b100 + 0b11 * 0b1111 +', [])
    assert results == [0b11011110]

    results = rpn.calculate('bin 0b110 hex 0x7 + oct 0o5 * bin 0b100 + dec 3 * 15 +', [])
    assert results == [222]

    results = rpn.calculate('bin 0xaa55 2 | 1 ~ &', [])
    assert results == [0b1010101001010110]


def test_networking():
    results = rpn.calculate('3232235521 hnl', [])
    assert results == [16820416]

    results = rpn.calculate('16820416 nhl', [])
    assert results == [3232235521]

    results = rpn.calculate('4096 hns', [])
    assert results == [16]

    results = rpn.calculate('16 nhs', [])
    assert results == [4096]


def test_errors(capsys):
    # Overflow
    results = rpn.calculate('-1 hnl', [])
    assert len(capsys.readouterr().err) > 0
    assert results == []

    # Not enough values in stack
    results = rpn.calculate('4 +', [])
    assert len(capsys.readouterr().err) > 0
    assert results == [4]

    # Invalid command
    results = rpn.calculate('foobar', [])
    assert len(capsys.readouterr().err) > 0
    assert results == []

    # ValueError
    results = rpn.calculate('10 acos', [])
    assert len(capsys.readouterr().err) > 0
    assert results == []

    # Zero division
    results = rpn.calculate('0 0 /', [])
    assert len(capsys.readouterr().err) > 0
    assert results == []

    # Assign variable to internal function name
    results = rpn.calculate('10 hex=', [])
    assert len(capsys.readouterr().err) > 0
    assert results == [10]

    # Will only evaluate macros with boundaries
    rpn.calculate('macro fullword 1 +', [])
    results = rpn.calculate('fullword=', [])
    assert len(capsys.readouterr().err) > 0
    assert results == []


def test_boolean():
    results = rpn.calculate('1 1 &&', [])
    assert results == [1]

    results = rpn.calculate('1 0 &&', [])
    assert results == [0]

    results = rpn.calculate('1 0 ||', [])
    assert results == [1]

    results = rpn.calculate('1 2 ^^', [])
    assert results == [3]

    results = rpn.calculate('1 !', [])
    assert results == [0]


def test_comparison():
    results = rpn.calculate('1 2 <', [])
    assert results == [1]

    results = rpn.calculate('2 1 <', [])
    assert results == [0]

    results = rpn.calculate('2 1 >', [])
    assert results == [1]

    results = rpn.calculate('2 1 >=', [])
    assert results == [1]

    results = rpn.calculate('1 1 ==', [])
    assert results == [1]

    results = rpn.calculate('1 10 ==', [])
    assert results == [0]

    results = rpn.calculate('1 10 <=', [])
    assert results == [1]


def test_variables():
    results = rpn.calculate('10 20 x= 30 + x + x', [])
    assert results == [60, 20]

    results = rpn.calculate('10 one= 20 two= 30 three= one two three', [])
    assert results == [10, 20, 30]

    results = rpn.calculate('10 20 30 x= oct x', [])
    assert results == [0o12, 0o24, 0o36]


def test_macros():
    results = rpn.calculate('macro foo 1000 +', [])
    assert results == []

    results = rpn.calculate('macro bar 1 +', [])
    assert results == []

    results = rpn.calculate('5 foo bar', [])
    assert results == [1006]

    results = rpn.calculate('macro mymacro 4 * ; 4 mymacro', [])
    assert results == [16]

    results = rpn.calculate('macro foo 1 + ; 1 foo foo', [])
    assert results == [3]


def test_one_shot(capsys):
    rpn.one_shot('dec 1 2 +')
    assert capsys.readouterr().out.strip() == '3'

    rpn.one_shot('9.123')
    assert capsys.readouterr().out.strip() == '9.123'
