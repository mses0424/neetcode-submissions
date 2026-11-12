class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        total = [[float('inf')] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if i == 0 and j == 0:
                    total[i][j] = grid[i][j]
                elif i == 0:
                    total[0][j] = grid[i][j] + total[i][j-1]
                elif j == 0:
                    total[i][0] = grid[i][j] + total[i-1][j]
                else:
                    total[i][j] = min(grid[i][j] + total[i-1][j], grid[i][j] + total[i][j-1])
        print(total)
        return total[row-1][col-1]