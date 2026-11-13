class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        total = [[0] * n for _ in range(n)]
        for i in range(n):
            total[i][i] = piles[i]
        for length in range(2,n+1):
            for start in range(0,n-length+1):
                end = start + length - 1
                left = piles[start] - total[start+1][end]
                right = piles[end] - total[start][end-1]
                total[start][end] = max(left,right)
        return (total[0][n-1] > 0)