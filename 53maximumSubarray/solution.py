# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums):
        #
        return sum(nums)


if __name__ == '__main__':
    #debugging
    solution = Solution()
    ans = solution.maxSubArray([1,2,3])
    print(ans)