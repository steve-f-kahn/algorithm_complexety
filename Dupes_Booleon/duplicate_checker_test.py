import pytest
from duplicate_checker import duplicate_checker 
class TestClass():
    def test_array_with_2_same_numbers_returns_true(self):
        assert duplicate_checker([1,1]) == True

    def test_array_with_2_2s_returns_true(self):
        assert duplicate_checker([2,2]) == True

    def test_array_with_2_different_numbers_returns_false(self):
        assert duplicate_checker([1,2]) == False
    
    def test_array_with_2_sets_of_dupes_returns_true(self):
        assert duplicate_checker([1,1,2,2]) == True

    def test_array_with_3_different_numbers_returns_false(self):
        assert duplicate_checker([1,2,3]) == False