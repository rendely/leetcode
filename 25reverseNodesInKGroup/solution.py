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
        if k == 1 or head.next is None:
            return head
        
        new_head = None
        new_tail = None
        count = 0
        is_next = head.next

        # keep going until all nodes used
        while is_next is not None:
        
        # if we run out of nodes before count == k, append rest as-


        

        return new_head

'''
Solution brainstorm #1

If k = 1, just return the head
If n <= 1, just return the head

Starting from the initial head, break it off into another list with a reference to the new head (next) and a cursor pointing at the end of this new list

Break of the new head and prepend to the new list, repeating this until you either reach K nodes in the new list OR there is no next node in the original list

If there is a next node, add it after the cursor, and then start prepending before the cursor as before.

If there is not a next node, we need to undo this batch of reversals

Example with even number k = 2
[1,2,3,4,5,6]
[1] [2,3,4,5,6]
[2,1] [3,4,5,6]
[2,1] [3] [4,5,6]
[2,1] [4,3] [5,6]
[2,1] [4,3] [5] [6]
[2,1] [4,3] [6,5]

Example with remainder k = 4
[1,2,3,4,5,6,7]
[1] [2,3,4,5,6,7]
[2,1] [3,4,5,6,7]
[3,2,1] [4,5,6,7]
[4,3,2,1] [5,6,7]
[4,3,2,1] [5] [6,7]
[4,3,2,1] [6,5] [7]
[4,3,2,1] [7,6,5] oops not enough


Solution brainstorm #2 maybe a cleaner recursive solution?
[1,2,3,4,5,6] with k = 2
reverse([1,2]) + reverse([3,4,5,6])
reverse([1,2]) + ( reverse([3,4]) + reverse([5,6])

''' 