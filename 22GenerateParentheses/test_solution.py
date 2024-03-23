import pytest
from solution import Solution


solution = Solution();

class TestSolution:
    def test_one(self):       
        assert solution.generateParenthesis(1) == ["()"]
    def test_three(self):       
        assert solution.generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]
