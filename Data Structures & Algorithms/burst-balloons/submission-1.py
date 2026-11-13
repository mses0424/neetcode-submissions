class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        val = [1] + nums + [1]
        n = len(val)
        total = [[0] * n for _ in range(n)]
        for length in range(3,n+1):
            for left in range(0,n-length+1):
                right = left + length - 1
                res = 0
                for k in range(left+1,right):
                    res = max(res, total[left][k] + total[k][right] + val[k] * val[left] * val[right])
                total[left][right] = res
        return total[0][n-1]