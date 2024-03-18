import pytest  
from src.area import calculate_area_square  
  
def test_calculate_area_square_negative():  
    with pytest.raises(TypeError):  
        calculate_area_square(-2)  
  
def test_calculate_area_square_string():  
    with pytest.raises(TypeError):  
        calculate_area_square("2")  
  
def test_calculate_area_square_list():  
    with pytest.raises(TypeError):  
        calculate_area_square([2])

# New function that validates the calculatiosn done by the application is accurate.
# My student ID is 100625770 so the output for the expected area of the square will be 70 * 70
def test_area_calculation():
    student_id_length = 70
    expected_area = 70 * 70
    assert calculate_area_square(student_id_length) == expected_area

