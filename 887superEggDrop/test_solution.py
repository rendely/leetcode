import pytest
from solution import Solution

solution = Solution();

class TestSolution:
    def test_ex1(self):
        assert solution.superEggDrop(1,2) == 2

    def test_ex2(self):
        assert solution.superEggDrop(3,14) == 4