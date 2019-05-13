import pytest
from reverse import reverse 

class TestClass:
    def test_reverse_returns_the_same_array_for_1_size(self):
        assert reverse([1]) == [1]

    def test_reverse_returns_an_array_that_has_been_reversed(self):
        assert reverse([2,1]) == [1,2]

    def test_reverse_returns_the_reverse_of_an_unordered_array(self):
        assert reverse([4,5,2,1,3]) == [3,1,2,5,4]

