from calculator import add_numbers, multiply_numbers

def test_add():
    assert add_numbers(2, 2) == 4

def test_multiply():
    assert multiply_numbers(3, 4) == 12
