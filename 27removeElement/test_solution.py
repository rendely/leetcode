import pytest
from solution import Solution

solution = Solution();

class TestSolution:
    def test_5(self):  
        input = [0,1,2,2,3,0,4,2]
        output = solution.removeElement(input, 2)
        assert(output == 5)
        expected_output = [0,1,4,0,3]
        assert(input[0:5] == expected_output)