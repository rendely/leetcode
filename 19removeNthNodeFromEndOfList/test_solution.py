import pytest
from solution import Solution, ListNode


solution = Solution();

class TestSolution:
    def test_two_nodes(self):
        one = ListNode(1)
        two = ListNode(2)
        three = ListNode(3)
        four = ListNode(4)
        five = ListNode(5)
        one.next = two
        two.next = three
        three.next = four
        four.next = five
        head = one
        assert solution.removeNthFromEnd(            
            head
            ,
            1
            ) == head
