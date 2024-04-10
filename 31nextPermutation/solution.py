# https://leetcode.com/problems/next-permutation/description/

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    def sort(self, nums: List[int], start_index=0) -> None:
        for i in range(start_index, len(nums)):
            for j in range(i+1,len(nums)):
                # print(i,j, nums) 
                left = nums[i]
                right = nums[j]
                if left > right:
                    nums[i] = right
                    nums[j] = left
                       
nums = [3,1,4,5,1,3,0]
Solution().sort(nums)
print(nums)
        

"""
Solution brainstorming
Start at the right hand side and if right most digit is greater than any digit 
to the left, insert in front of the first digit it's greater than. 

** Can't just insert though, sometimes you need to resort numbers later -> need a rule for this

If none are greater, start at second to last digit and check again. 

If you reach left hand side and cannot swap we need to reverse
all the digits. Do this by swapping pair by pair from right to left and repeat
in loop but stopping sooner each time

Testing on example:

[1,2,4,3] => [1,3,4,2] WRONG
[1,2,4,3] => [1,3,2,4] RIGHT

[1,4,3,2] => [2,1,4,3] WRONG
[1,4,3,2] => [2,1,3,4] RIGHT

[1,2,3,4] => [1,2,4,3] RIGHT


Example going up
1234
1243 swap last and second last
1324 swap last and second last and then middle
1342
1423
1432
2134

"""

"""
Swap sorting algorithm

3121
1321
1231
1213



"""