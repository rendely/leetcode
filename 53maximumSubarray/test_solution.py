import pytest
from solution import Solution

solution = Solution();

class TestSolution:
    def test_length_one(self):
        assert solution.maxSubArray([-4]) == -4

    def test_sorted(self):
        assert solution.maxSubArray([-1,0,1]) == 1
    
    def test_unsorted(self):
        assert solution.maxSubArray([-1,-2,-3]) == -1
    
    def test_entire_length(self):
        assert solution.maxSubArray([3,-2, 0, 0, 0, 0, 1, 3]) == 5

    def test_alternating(self):
        assert solution.maxSubArray([1,-1, 1, -1, 1, -1, 1]) == 1        
