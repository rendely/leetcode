# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        return f'<ListNode val={self.val} next={self.next}>'
        

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        next_node = head.next
        index = [head]
        while next_node:
            index.append(next_node)
            next_node = next_node.next
        length = len(index)
        if length == 1:
            return 
        if n == length:
            return index[1]
        if n == 1:
            index[-2].next = None
        else:            
            index[length-n-1].next = index[length-n+1]
        
        return head


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
one.next = two
two.next = three
three.next = four
four.next = five

solution = Solution()

print(solution.removeNthFromEnd(one, 2))