#to run the tests:
#command line: nosetests -v test_with_nose.py


from mathfunctions import add, subtract, multiply, divide


def test_add_3_4():
    assert add(3, 4) == 7


def test_subtract_3_4():
    assert subtract(3, 4) == -1


def test_multiply_3_4():
    assert multiply(3, 4) == 12


def test_divide_3_4():
    assert divide(3, 4) == 0.75



