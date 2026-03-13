from calculator import Calculator

def test_add():
    calc = Calculator(10, 5)
    assert calc.add() == 15

def test_sub():
    calc = Calculator(10, 5)
    assert calc.sub() == 5

def test_mul():
    calc = Calculator(10, 5)
    assert calc.mul() == 50

def test_divide():
    calc = Calculator(10, 5)
    assert calc.divide() == 2

def test_sqrt():
    calc = Calculator(10, 5)
    assert calc.sqrt == 100