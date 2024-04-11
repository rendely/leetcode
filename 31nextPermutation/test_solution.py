import pytest
from solution import Solution

solution = Solution();

class TestSolution:
    def test_base(self):  
        input = [1,2,3]
        output = solution.nextPermutation(input)
        expected_output = [1,3,2]
        assert output == expected_output

    def test_four_digits(self):  
        input = [1,2,4,3]
        output = solution.nextPermutation(input)
        expected_output = [1,3,2,4]
        assert output == expected_output

    def test_loop_around(self):  
        input = [3,2,1]
        output = solution.nextPermutation(input)
        expected_output = [1,2,3]
        assert output == expected_output