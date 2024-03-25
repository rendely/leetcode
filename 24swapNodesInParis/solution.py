# https://leetcode.com/problems/swap-nodes-in-pairs/description/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        vals = [self.val]
        next = self.next
        while next:
            vals.append(next.val)
            next = next.next
        return f'{vals}'
    
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return head
    
input = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
print(input)
output = Solution().swapPairs(input)
print(output)