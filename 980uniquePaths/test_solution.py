import pytest
from solution import Solution

solution = Solution();

class TestSolution:
    def test_ex1(self):
        assert solution.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]) == 2

    def test_ex2(self):
        assert solution.rob([[1,0,0,0],[0,0,0,0],[0,0,0,2]]) == 4