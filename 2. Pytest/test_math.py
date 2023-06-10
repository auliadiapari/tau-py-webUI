"""
This module contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example.
"""

# --------------------------------------------------------------------------------
# A most basic test function
# --------------------------------------------------------------------------------

def test_one_plus_one():
  assert 1 + 1 == 2

def test_one_plus_two():
    a = 1
    b = 2
    if a + b == 3:
        print("The calculation is correct")
        