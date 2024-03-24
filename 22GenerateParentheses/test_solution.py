import pytest
from solution import Solution


solution = Solution();

class TestSolution:
    def test_one(self):       
        assert set(solution.generateParenthesis(1)) == set(["()"])
    def test_three(self):       
        assert set(solution.generateParenthesis(3)) == set(["((()))","(()())","(())()","()(())","()()()"])
