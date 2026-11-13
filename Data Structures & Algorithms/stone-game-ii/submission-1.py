from typing import List
from functools import cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * n
        suffix[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]
        total = [[-1] * (n+1) for _ in range(n)]
        def dfs(i: int, M: int) -> int:
            if i + 2 * M >= n:
                return suffix[i]
            if total[i][M] != -1:
                return total[i][M]
            max_stones = 0
            for x in range(1, 2 * M + 1):
                score = suffix[i] - dfs(i + x, max(M, x))
                max_stones = max(max_stones, score)
            total[i][M] = max_stones
            return max_stones
        return dfs(0, 1)