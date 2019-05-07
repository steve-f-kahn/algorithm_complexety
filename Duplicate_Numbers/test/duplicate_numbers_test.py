import os
import sys
import pytest

sys.path.insert(0, os.path.abspath('lib'))

from duplicate_numbers import check_dupes
class TestClass:
    
    def test_duplicate_is_given_array_with_2_1s_and_returns_array_with_1(self):
        test_array = [1,1]
        expected_output = [1]
        assert check_dupes(test_array) == expected_output

    def test_duplicate_is_given_array_with_2_1s_a_2_and_returns_array_with_1(self):
        test_array = [1,1,2]
        expected_output = [1]
        assert check_dupes(test_array) == expected_output

    def test_duplicate_is_given_array_with_2_2s_and_a_1_returns_array_with_2(self):
        test_array = [2,2,1]
        expected_output = [2]
        assert check_dupes(test_array) == expected_output

    def test_1_2_3_returns_empty_array(self):
        test_array = [1,2,3]
        expected_output = []
        assert check_dupes(test_array) == expected_output

    def test_an_array_with_multiple_dupes(self):
        test_array = [1,1,1,2,2,3]
        expected_output = [1,2]
        assert check_dupes(test_array) == expected_output

    def test_an_array_that_has_a_string(self):
        test_array = ["A string"]
        expected_output = []
        assert check_dupes(test_array) == expected_output

    def test_an_array_that_has_two_strings_that_are_the_same(self):
        test_array = ["A string", "A string"]
        expected_output = []
        assert check_dupes(test_array) == expected_output

    def test_an_array_that_has_a_string_and_two_intergers_that_are_the_same(self):
        test_array = ["A string", 1, 1]
        expected_output = [1]
        assert check_dupes(test_array) == expected_output

    def test_an_array_that_has_two_booleons_that_are_the_same(self):
        test_array = [True, True]
        expected_output = []
        assert check_dupes(test_array) == expected_output
