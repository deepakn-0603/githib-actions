from calculator import Calculator

def test_add():
    calc = Calculator.add(10, 5)
    assert calc == 15

def test_sub():
    calc = Calculator.sub(10, 5)
    assert calc == 5

def test_mul():
    calc = Calculator.mul(10, 5)
    assert calc == 50

def test_divide():
    calc = Calculator.divide(10, 5)
    assert calc == 2

def test_sqrt():
    calc = Calculator.sqrt(10, 5)
    assert calc == 100