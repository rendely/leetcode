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
        # Check if only 0 or 1 nodes
        if head is None or head.next is None:
            return head
        
        # Do the first swap and keep that first head to return
        a = head
        b = head.next
        return_head = b
        a.next = b.next
        b.next = a

        # Go through rest of pairs if they exist
        prior = a
        while prior.next and prior.next.next:
            a = prior.next
            b = prior.next.next
            prior.next = b 
            a.next = b.next
            b.next = a 
            prior = a

        return return_head
    
input = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
print(input)
output = Solution().swapPairs(input)
print(output)

# If empty return same empty 
# If one value, return as is
# If two nodes, swap them
# If three nodes, swap first two
# We need to detect to stop when there are either 0 or only 0 nodes after the current two working set
# To swap nodes A and B, we need to set B.next to A, and A.next to B.next
# Additionally, we need to ensure whatever node was before A now points to B
