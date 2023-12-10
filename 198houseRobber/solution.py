# https://leetcode.com/problems/house-robber/


class Solution:
    def robRecursiveBrute(self, nums):
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))              


'''
Notes
Lets try to break down the example given into smaller sub problems
[2,7,9,3,1]
For any pair of numbers pick the greater one
2,7 -> 7
7,9 -> 9
9,3 -> 9
3,1 -> 3
As you move from left to right, pick the greater of the pair if it will not 
prevent you from getting an even bigger maximum by choosing adjacent in the next pair
E.g.
between 2 and 7 you can't choose seven, because then in next pair your max total is 10
whereas if you pick 2 your max total is 11
Should be solvable in O(n)

[2,50,1,50,100]
In this new example it's not enough to look at first four nums
if you did you'd pick 50 and 50
[1,1,90,100,20]
In this example, also not good algo to start with largest number, you'd miss 90 + 20
You would never skip more than two in a row because you'd be giving up a free num

'''