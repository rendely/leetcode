import pytest
from solution import Solution

solution = Solution();

class TestSolution:
    def test_one(self):  
        s = "barfoothefoobarman"
        words = ["foo","bar"]
        output = solution.findSubstring(s, words)
        expected_output = [0,9]
        assert output == expected_output   

    def test_two(self):  
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","word"]
        output = solution.findSubstring(s, words)
        expected_output = []
        assert output == expected_output     