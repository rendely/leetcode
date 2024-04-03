# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_seen = None
        unique_count = 0
        cursor = 0
        for i,v in enumerate(nums):
            curr_value = nums[i]
            if curr_value == last_seen:
                pass
            elif last_seen is None or nums[i] > last_seen:
                nums[cursor] = curr_value
                cursor = cursor + 1                
                unique_count = unique_count + 1
                last_seen = curr_value
        
        return unique_count
                

input = [1,1,2]
Solution().removeDuplicates(input)
print(input)
    
'''Solution notes
This should be possible O(n), go through list once.
Talking out loud through a solution
input = [0,0,1,1,1,2,2,3,3,4]
1: add 0 to seen_set, set cursor to 1 where next unique number will go 
2: since 0 is seen already, do nothing, leave cursor at 1 so next unique number can be slotted there
3: since 1 is unique, add to seen_set, push it to cursor location, and update cursor++
4: since 1 is seen, leave cursor alone
5: since 1 is seen, leave cursor alone
6: since 2 is new, add to seen_set, push to cursor location, cursor++

We need to go through every element since even the last one could be new unique one in set

Upon revising, we don't actually need a seen_set, we just need a last_seen
and can check if curr value is > last_seen since they are sorted in 
non-decreasing order
'''    