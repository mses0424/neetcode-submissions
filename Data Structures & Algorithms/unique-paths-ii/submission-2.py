class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid[0])
        col = len(obstacleGrid)
        total = [[0] * row for _ in range(col)]
        for k in range(row):
            for l in range(col):
                if obstacleGrid[l][k]:
                    total[l][k] = 0
                elif  k == 0 and l == 0:
                    total[k][l] = 1
                elif k == 0:
                    total[l][k] = total[l-1][k]
                elif l == 0:
                    total[l][k] = total[l][k-1]
                else:
                    total[l][k] = total[l-1][k] + total[l][k-1]
        print(total)
        return total[col-1][row-1]