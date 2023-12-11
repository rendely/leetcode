# https://leetcode.com/problems/unique-paths-iii/


class Solution:
    def uniquePathsIII(self,grid, start=None, end=None, num_empty=None, visited=None):
        if len(grid) == 0:
            return 0
        # get start, end, num_empty
        if start is None:
            start, end, num_empty = self.getStartEnd(grid)  
            visited = {start}
        # If a recursive call update visited
        visited.add(start)

        # Check if available paths
        available_paths = self.getAvailablePaths(grid, start, visited)
       
        i,j = start
        if len(available_paths) == 0:
            # return condition for succeeded path   
            if grid[i][j] == 2 and len(visited) == num_empty+2:
                return 1
            # return condition for failed path
            else:
                return 0

        # print(f' {available_paths=},{visited=}, {num_empty=}')

        valid_paths = 0        
        # for each path, check if it's a valid path and return count of subpaths
        for path in available_paths:
            valid_paths += self.uniquePathsIII(grid, path, end, num_empty, visited.copy())

        return valid_paths
    
    def getAvailablePaths(self, grid, cell, visited={}):
        available = []
        i,j = cell
        # try top
        if (i > 0 and grid[i-1][j] in [0,2] and (i-1,j) not in visited):
            available.append((i-1,j))
        # try bottom
        if (i < len(grid)-1 and grid[i+1][j] in [0,2] and (i+1,j) not in visited):
            available.append((i+1,j))
        # try left
        if (j > 0 and grid[i][j-1] in [0,2] and (i,j-1) not in visited):
            available.append((i,j-1))
        # try right    
        if (j < len(grid[0])-1 and grid[i][j+1] in [0,2] and (i,j+1) not in visited):
            available.append((i,j+1))
        return available     
        
    def getStartEnd(self, grid):
        start = None
        end = None 
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_empty = 0
        for i in range(0, num_rows):
            for j in range(0, num_cols):
                if grid[i][j] == 1:
                    start = (i,j)
                if grid[i][j] == 2:
                    end = (i,j)
                if grid[i][j] == 0:
                    num_empty = num_empty +1
        return (start, end,  num_empty)
        
if __name__ == '__main__':
    #debugging
    solution = Solution()
    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    # grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    # grid = [[1,0,2]]
    # startEnd = solution.getStartEnd(grid)
    # print(startEnd)
    # avail = solution.getAvailablePaths(grid, (1, 1))
    # print(avail)
    ans = solution.uniquePathsIII(grid)
    print(f'{ans=}')

'''
Notes
First run a method to find start and end
Beginning at the start, run a method to find available moves
For each move add it to a list of paths if it's a valid move.
Valid move should be a recursive method that checks if that valid move has
valid moves that have valid moves that end at end point and have explored all empty squares
Recursive returns true if there's only one move left which is end square, and 
number of visited squares == number of empty squares
'''
