import pytest
from main import calculate_square_area  # Importing the function

# Test for valid calculations
def test_calculate_area_student_id():
    assert calculate_square_area(91) == 8281  # 91^2 = 8281

def test_calculate_area_small_number():
    assert calculate_square_area(5) == 25  # 5^2 = 25

def test_calculate_area_large_number():
    assert calculate_square_area(100) == 10000  # 100^2 = 10000

def test_calculate_area_decimal():
    assert calculate_square_area(2.5) == 6.25  # 2.5^2 = 6.25

# Test for negative values (should raise ValueError)
def test_calculate_area_negative():
    with pytest.raises(ValueError, match="Side length cannot be negative! Please enter a positive number."):
        calculate_square_area(-81)

# Test for invalid input (string)
def test_calculate_area_invalid_input():
    with pytest.raises(TypeError, match="Invalid input! Please enter a number."):
        calculate_square_area("hello")