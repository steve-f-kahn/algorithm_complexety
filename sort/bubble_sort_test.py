import pytest
import sys
import os 
sys.path.append(os.path.abspath('../shuffle'))
from shuffle import shuffle
from bubble_sort import bubble_sort as sort 

class TestClass:
    def test_sort_returns_an_array_that_is_sorted_lowest_to_highest(self):
        assert sort([2,1]) == [1,2]

    def test_an_allready_sorted_array_returns_the_same_array(self):
        assert sort([1,2]) == [1,2]

    def test_a_more_complicated_array_is_sorted_lowest_to_highest(self):
        assert sort([4,2,3,1]) == [1,2,3,4]

    def test_a_large_array_is_sorted_lowest_to_highest(self):
        assert sort(shuffle([1,2,3,4,5,6,7,8,9,10])) == [1,2,3,4,5,6,7,8,9,10]