# https://leetcode.com/problems/reverse-nodes-in-k-group/description/

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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass