import pytest
from solution import Solution, ListNode

solution = Solution();

class TestSolution:
    def test_4_K_2(self):  
        input = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
        output = solution.reverseKGroup(input, 2)
        expected_output = ListNode(2,ListNode(1,ListNode(4,ListNode(3))))
        assert f'{output}' == f'{expected_output}'

    def test_4_K_3(self):  
        input = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
        output = solution.reverseKGroup(input, 3)
        expected_output = ListNode(3,ListNode(2,ListNode(1,ListNode(4))))
        assert f'{output}' == f'{expected_output}'

    def test_5_K_3(self):  
        input = ListNode(1,ListNode(2,ListNode(3,ListNode(4, ListNode(5)))))
        output = solution.reverseKGroup(input, 3)
        expected_output = ListNode(3,ListNode(2,ListNode(1,ListNode(4, ListNode(5)))))
        assert f'{output}' == f'{expected_output}'