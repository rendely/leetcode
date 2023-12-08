# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums):
        max_so_far = None
        for start in range(0,len(nums)):
            for end in range(start+1, len(nums)+1):
                this_sum = sum(nums[start:end])
                if  max_so_far is None or this_sum > max_so_far:
                    max_so_far = this_sum
        return max_so_far
    def maxSubArrayNaive(self, nums):
        max_so_far = None
        for start in range(0,len(nums)):
            for end in range(start+1, len(nums)+1):
                this_sum = sum(nums[start:end])
                if  max_so_far is None or this_sum > max_so_far:
                    max_so_far = this_sum
        return max_so_far


if __name__ == '__main__':
    #debugging
    solution = Solution()
    ans = solution.maxSubArray([1,2,3])
    print(ans)