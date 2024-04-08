# https://leetcode.com/problems/next-permutation/description/

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

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

"""