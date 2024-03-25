import pytest
from solution import Solution, ListNode


solution = Solution();

class TestSolution:
    def test_one(self):  
        input = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
        output = solution.swapPairs(input)
        expected_output = ListNode(2,ListNode(1,ListNode(4,ListNode(3))))
        assert output == expected_output