import pytest
from solution import Solution

solution = Solution();

class TestSolution:
    def test_ex1(self):
        assert solution.rob([1,2,3,1]) == 4

    def test_ex2(self):
        assert solution.rob([2,7,9,3,1]) == 12