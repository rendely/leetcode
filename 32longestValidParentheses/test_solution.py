import pytest
from solution import Solution

solution = Solution();

class TestSolution:
    def test_zero(self):  
        s = ""
        output = solution.longestValidParentheses(s)
        expected_output = 0
        assert output == expected_output

    def test_two(self):  
        s = "(()"
        output = solution.longestValidParentheses(s)
        expected_output = 2
        assert output == expected_output

    def test_four(self):  
        s = ")()())"
        output = solution.longestValidParentheses(s)
        expected_output = 4
        assert output == expected_output
    
    def test_four_b(self):
        s = "(())("
        output = solution.longestValidParentheses(s)
        expected_output = 4
        assert output == expected_output
