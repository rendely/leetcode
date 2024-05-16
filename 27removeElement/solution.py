# https://leetcode.com/problems/remove-element/description/

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1 and nums[0] == val:
            nums[0] = None
            return 0        

        front = 0
        back = len(nums)-1
        keep_count = 0

        while back > front:            
            if nums[front] == val:
                back_num = nums[back]
                while back_num == val and back > front:
                    nums[back] = None
                    back = back - 1
                    back_num = nums[back]
                nums[front] = back_num 
                nums[back] = None
                back = back -1 
                keep_count = keep_count + 1
            else:            
                keep_count = keep_count + 1
            front = front + 1
        
        return keep_count+1
    

input = [3,2,2,3]
print(input)
sol = Solution()
ans = sol.removeElement(input, 3)
print(ans,input)

'''
Solution notes

Need to remove occurences in place
Move removed occurences to end of list
order of kept numbers doesnt matter


Idea to have one cursor start at the front, another at the back
whenever front cursor finds value to remove it checks if it can replace it with back cursor
If not it removes back cursor and moves it one left until it finds one it can swap
Unless back cursor meets front cursor in which case all removed up to that point
'''    