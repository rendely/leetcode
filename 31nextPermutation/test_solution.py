import pytest
from solution import Solution

solution = Solution();

class TestSolution:
    def test_one(self):  
        input = [3,2,1]
        output = solution.nextPermutation(input)
        expected_output = [1,2,3]
        assert output == expected_output