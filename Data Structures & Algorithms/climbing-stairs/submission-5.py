class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        total = [0,1,2]
        for i in range(3,n+1):
            total.append(total[i-1]+total[i-2])
        return total[n]