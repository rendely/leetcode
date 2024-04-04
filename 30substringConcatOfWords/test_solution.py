import pytest
from solution import Solution

solution = Solution();

class TestSolution:
    def test_two(self):  
        s = "barfoothefoobarman"
        words = ["foo","bar"]
        output = solution.findSubstring(s, words)
        expected_output = [0,9]
        assert output == expected_output   

    def test_none(self):  
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","word"]
        output = solution.findSubstring(s, words)
        expected_output = []
        assert output == expected_output     

    def test_dupe_words(self):  
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","good"]
        output = solution.findSubstring(s, words)
        expected_output = [8]
        assert output == expected_output