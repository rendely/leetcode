# https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums):
        pass


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
'''