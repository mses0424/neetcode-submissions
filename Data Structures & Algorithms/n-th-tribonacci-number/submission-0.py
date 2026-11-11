class Solution:
    def tribonacci(self, n: int) -> int:
        total = [0,1,1]
        if n <= 2:
            return total[n]
        for i in range(3,n+1):
            total.append(total[i-1]+total[i-2]+total[i-3])
        return total[n]