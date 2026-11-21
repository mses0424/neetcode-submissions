class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxi = 0
        def dfs(i,j):
            total = 0
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return total
            grid[i][j] = 0
            total += 1
            return total + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxi = max(maxi, dfs(i,j))
        return maxi