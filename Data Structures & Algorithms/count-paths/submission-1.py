import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = m + n - 2
        ans = math.factorial(total) / (math.factorial(n-1) * math.factorial(m-1))
        return int(ans)