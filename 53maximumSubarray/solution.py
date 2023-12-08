# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums):
        max_so_far = None
        for start in range(0,len(nums)):  
            sum_so_far = 0
            for end in range(start, len(nums)):
                sum_so_far = sum_so_far + nums[end]
                if  max_so_far is None or sum_so_far > max_so_far:
                    max_so_far = sum_so_far
        return max_so_far

    def maxSubArrayNaive(self, nums):
        max_so_far = None
        for start in range(0,len(nums)):
            for end in range(start+1, len(nums)+1):
                this_sum = sum(nums[start:end])
                if  max_so_far is None or this_sum > max_so_far:
                    max_so_far = this_sum
        return max_so_far


'''
The naive solution is O(n^3) beacuse of sum operation
'''

if __name__ == '__main__':
    #debugging
    solution = Solution()
    ans = solution.maxSubArray([1,2,3])
    print(ans)