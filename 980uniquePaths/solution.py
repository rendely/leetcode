# https://leetcode.com/problems/unique-paths-iii/


class Solution:
   def uniquePathsIII(self, grid):
        pass
   def getStartEnd(self, grid):
        num_rows = len(grid)
        num_cols = len(grid[0])
        for i in range(0, num_rows):
            for j in range(0, num_cols):
                if grid[i][j] == 1:
                    start = (i,j)
                if grid[i][j] == 2:
                    end = (i,j)
        return {"start": start, "end": end}
        
'''
Notes

'''

if __name__ == '__main__':
    #debugging
    solution = Solution()
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    startEnd = solution.getStartEnd(grid)
    print(startEnd)
    ans = solution.uniquePathsIII([[]])
    print(f'{ans=}')