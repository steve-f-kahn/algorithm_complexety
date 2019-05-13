import pytest
from shuffle import shuffle

class TestClass:
    def test_shuffle_returns_the_same_array_for_a_1_size_array(self):
        assert shuffle([1]) == [1]

    def test_shuffle_returns_a_different_array_when_randomness_stubbed(self):
        assert shuffle([1,2],1) == [2,1]

    def test_shuffle_returns_a_different_array_when_randomness_stubbed(self):
        assert shuffle([1,2,3,4,5],1) == [2,1,5,4,3]