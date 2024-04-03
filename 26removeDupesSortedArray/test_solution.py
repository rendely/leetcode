import pytest
from solution import Solution

solution = Solution();

class TestSolution:
    def test_two(self):  
        input = [1,1,2]
        output = solution.removeDuplicates(input)
        expected_output = 2
        assert output == expected_output
        expected_output_array = [1,2]
        print(f'{output=}, {input=}')
        for i, v in enumerate(expected_output_array):
            assert expected_output_array[i] == input[i]
    
    def test_five(self):
        input = [0,0,1,1,1,2,2,3,3,4]
        output = solution.removeDuplicates(input)
        expected_output = 5
        assert output == expected_output
        expected_output_array = [0,1,2,3,4]
        print(f'{output=}, {input=}')
        for i,v in enumerate(expected_output_array):
            assert expected_output_array[i] == input[i]
        