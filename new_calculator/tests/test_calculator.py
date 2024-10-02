import pytest
from calculator.calculator import Calculator

@pytest.fixture(autouse=True)
def reset_calculator_history():
    Calculator.history.clear()  # Clear history before each test

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert Calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (-1, -1, 0),
    (0, 1, -1)
])
def test_subtract(a, b, expected):
    assert Calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, 1, -1),
    (0, 5, 0)
])
def test_multiply(a, b, expected):
    assert Calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 2, 3),
    (1, 1, 1),
    (0, 1, 0)
])
def test_divide(a, b, expected):
    assert Calculator.divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(1, 0)

def test_history():
    Calculator.add(1, 2)
    assert len(Calculator.history) == 1
    last_calculation = Calculator.get_last_calculation()
    assert last_calculation.operation == "1 + 2"
    assert last_calculation.result == 3

# New test using generated records
def test_calculator_operations(generate_records):
    for a, b, operation in generate_records:
        if operation == 'add':
            expected = a + b
            assert Calculator.calculate(a, b, operation) == f"The result of {a} add {b} is equal to {expected}"
        elif operation == 'subtract':
            expected = a - b
            assert Calculator.calculate(a, b, operation) == f"The result of {a} subtract {b} is equal to {expected}"
        elif operation == 'multiply':
            expected = a * b
            assert Calculator.calculate(a, b, operation) == f"The result of {a} multiply {b} is equal to {expected}"
        elif operation == 'divide':
            if b == 0:
                assert Calculator.calculate(a, b, operation) == "An error occurred: Cannot divide by zero."
            else:
                expected = a / b
                assert Calculator.calculate(a, b, operation) == f"The result of {a} divide {b} is equal to {expected}"
        else:
            assert Calculator.calculate(a, b, operation) == f"Unknown operation: {operation}"
