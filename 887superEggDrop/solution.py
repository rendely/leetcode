# https://leetcode.com/problems/super-egg-drop/
import math 

class Solution:
    def superEggDrop(self, k: int,n: int) -> int:
        drops = 0
        while (k > 1):
            n = math.ceil(n / 2)
            k = k -1 
            drops = drops + 1
        return n + drops


if __name__ == '__main__':
    solution = Solution()
    ans = solution.superEggDrop(1,2)
    print(f'Does 2=={ans=}')

'''
Solution notes
- Seems like a binary search, but you can only binary search until you have one
  egg remaining
- Once you have one egg you start at the lowest unknown floor and,keep going up
  until you reach the breaking floor
- Seems more like a math equation than an algorithm

Examples
- If k = 1 and n = 1, answer is 1
- If k = 1 and n = 2, answer is 2
- If k = 1 and n = 3, answer is 3
- So for k = 1, answer is n

- If k = 2 and n = 3, answer is 2
- If k = 2 and n = 4, answer is 3 since you can guess it's 2nd floor, if it 
  breaks you try floor 1 as well. if it doesnt break you try floor 3 and then 4
- If k = 2 and n = 5, answer is 3 since you can guess floor 3, if it breaks,
  try 1 and 2. if it doesn't try 4, then 5. 
- If k = 2 and n = 10, answer is 5
- So for k = 2, it's floor((n-1) / 2) +1

- If k = 3 and n = 5, answer is 3 since you can guess floor 3, if it breaks,
  try 1 and 2. if it doesn't try 4, then 5. having more eggs doesnt speed up
  since you can't divide further on the next step

So I think the algo is, divide in half, rounding up until you have 1 egg, at that point return number of steps

TODO: need to modify math for off by one since it breaks at higher than f

Problem statement
You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.

Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.

Return the minimum number of moves that you need to determine with certainty what the value of f is
'''