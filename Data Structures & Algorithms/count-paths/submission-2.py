import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # total = m + n - 2
        # ans = math.factorial(total) / (math.factorial(n-1) * math.factorial(m-1))
        # return int(ans)
        total = [[0] * n for _ in range(m)]
        for i in range(m):
            total[i][0] = 1
        for j in range(n):
            total[0][j] = 1
        for k in range(1,n):
            for l in range(1,m):
                total[l][k] = total[l][k-1] + total[l-1][k]
        return total[m-1][n-1]