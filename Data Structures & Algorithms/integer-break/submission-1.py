class Solution:
    def integerBreak(self, n: int) -> int:
        total = [0] * (n+1)
        total[1] = 1
        total[2] = 1
        for i in range(3,n+1):
            ans = 0
            for j in range(1,(i//2)+1):
                first = max(total[j],j)
                second = max(total[i-j],i-j)
                ans = max(ans, first*second)
            total[i] = ans
        print(total)
        return total[n]