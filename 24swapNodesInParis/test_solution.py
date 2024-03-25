import pytest
from solution import Solution


solution = Solution();

class TestSolution:
    def test_one(self):  
        input = [1,2,3,4]     
        output = solution.swapPairs(input)
        expected_output = [2,1,4,3]
        assert output == expected_output