"""
This module contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example.
"""

import pytest

# --------------------------------------------------------------------------------
# A most basic test function
# --------------------------------------------------------------------------------

@pytest.mark.math
def test_one_plus_one():
  assert 1 + 1 == 2

# --------------------------------------------------------------------------------
# A test function to show assertion introspection
# if the var c = 0 meaning the calculation is false and error will shown
# --------------------------------------------------------------------------------

@pytest.mark.math
def test_one_plus_two():
  a = 1
  b = 2
  c = 3
  # c = 0
  assert a + b == c

# --------------------------------------------------------------------------------
# A test function that verifies an exception
# Pytest could not throw an excepts division by zero, so need to raise the error to pass
#     def test_divided_by_zero():
# >     num = 1 / 0
# E     ZeroDivisionError: division by zero

# 2. Pytest\test_math.py:32: ZeroDivisionError
# --------------------------------------------------------------------------------

@pytest.mark.math
def test_divided_by_zero():
# Raises = To catch exceptions raised by the pytest framework.
# The "with" statement executes additional "enter" and "exit" logic for handling raised exceptions.
  with pytest.raises(ZeroDivisionError) as e:
# Add an "as" clause to the end of the "with" statement to store the exception into a variable.
    num = 1 / 0
  
  assert 'division by zero' in str(e.value)


# --------------------------------------------------------------------------------
# A parametrized test function
# --------------------------------------------------------------------------------

products = [
  (2, 3, 6),            # postive integers
  (1, 99, 99),          # identity
  (0, 99, 0),           # zero
  (3, -4, -12),         # positive by negative
  (-5, -5, 25),         # negative by negative
  (2.5, 6.7, 16.75)     # floats
]

@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
  assert a * b == product

