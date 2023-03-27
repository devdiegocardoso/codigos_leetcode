from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        lines = len(grid)
        columns = len(grid[0])
        land_sizes = [0]
        for i in range(lines):
            for j in range(columns):
                if grid[i][j] == 1:
                    size = self.count_terrain(grid,i,j)
                    land_sizes.append(size)
        return max(land_sizes)

    def count_terrain(self,grid: List[List[int]],r,c):
        counter = 0
        if grid[r][c] == 1:
            counter = 1
            grid[r][c] = 0
            if r >= 1:
                counter += self.count_terrain(grid,r-1,c)
            if c >= 1:
                counter +=  self.count_terrain(grid,r,c-1)
            if r < len(grid) - 1:
                counter += self.count_terrain(grid,r+1,c)
            if c < len(grid[0]) - 1:
                counter += self.count_terrain(grid,r,c+1)
        return counter
        
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
r = Solution().maxAreaOfIsland(grid)
print(r)