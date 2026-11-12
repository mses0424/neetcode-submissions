class Solution:
    def numSquares(self, n: int) -> int:
        total = [float('inf')] * (n+1)
        total[0] = 0
        for i in range(1,n+1):
            j = 1
            while j * j <= i:
                total[i] = min(total[i], total[i-j*j] + 1)
                j += 1
        return total[n]