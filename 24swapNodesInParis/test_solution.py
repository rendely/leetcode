import pytest
from solution import Solution, ListNode


solution = Solution();

class TestSolution:
    def test_empty(self):  
        input = None
        output = solution.swapPairs(input)
        expected_output = None
        assert f'{output}' == f'{expected_output}'

    def test_one(self):  
        input = ListNode(1)
        output = solution.swapPairs(input)
        expected_output = ListNode(1)
        assert f'{output}' == f'{expected_output}'

    def test_two(self):  
        input = ListNode(1,ListNode(2))
        output = solution.swapPairs(input)
        expected_output = ListNode(2,ListNode(1))
        assert f'{output}' == f'{expected_output}'

    def test_three(self):  
        input = ListNode(1,ListNode(2,ListNode(3)))
        output = solution.swapPairs(input)
        expected_output = ListNode(2,ListNode(1,ListNode(3)))
        assert f'{output}' == f'{expected_output}'
    
    def test_four(self):  
        input = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
        output = solution.swapPairs(input)
        expected_output = ListNode(2,ListNode(1,ListNode(4,ListNode(3))))
        assert f'{output}' == f'{expected_output}'

    def test_seven(self):  
        input = ListNode(2,ListNode(5,ListNode(3,ListNode(4, ListNode(6, ListNode(2, ListNode(2)))))))
        output = solution.swapPairs(input)
        expected_output = ListNode(5,ListNode(2,ListNode(4,ListNode(3, ListNode(2, ListNode(6, ListNode(2)))))))
        assert f'{output}' == f'{expected_output}'