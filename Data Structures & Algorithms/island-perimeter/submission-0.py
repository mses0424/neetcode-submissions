class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total += 4
                    if 0 <= i+1 < len(grid) and grid[i+1][j] == 1:
                        total -= 1
                    if 0 <= i-1 < len(grid) and grid[i-1][j] == 1:
                        total -= 1
                    if 0 <= j+1 < len(grid[0]) and grid[i][j+1] == 1:
                        total -= 1
                    if 0 <= j-1 < len(grid[0]) and grid[i][j-1] == 1:
                        total -= 1
        return total
                    