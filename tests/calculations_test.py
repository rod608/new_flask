from calculator.calculations import Calculation


# Test each operation (create), test each getResult method
def test_placeholder():
    Calculation.create((1, 2))
    assert (1 + 1) == 2
