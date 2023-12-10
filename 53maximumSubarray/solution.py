# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums):
        max_so_far = nums[0]
        sum_so_far = nums[0]
        for i in range(1,len(nums)):  
            if nums[i] > sum_so_far + nums[i]:
                sum_so_far = nums[i]
            else:
                sum_so_far += nums[i]
            if sum_so_far > max_so_far:
                max_so_far = sum_so_far
        return max_so_far

    def maxSubArrayOofNsquared(self, nums):
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
Notes
The naive solution is O(n^3) because of sum operation
I made that faster to O(n^2) but still timing out on leetcode submission
By hand I tested out a concept https://docs.google.com/spreadsheets/d/1nis0TIXi5VBVuWhIj3r0iEdmIuBGSCNapnJq8Npk_wA/edit#gid=0
In particular test subarrays with negative value
If you start expanding your subarray, but restart it as soon as your next num
is greater than your current subarray + next num

'''

if __name__ == '__main__':
    #debugging
    solution = Solution()
    ans = solution.maxSubArray([1,2,3])
    print(ans)
    ans = solution.maxSubArray([-10,-1,-1,-10])
    print(ans)
    ans = solution.maxSubArray([3,-2, 0, 0, 0, 0, 1, 3])
    print(ans)