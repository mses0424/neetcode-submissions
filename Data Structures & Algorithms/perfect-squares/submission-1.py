class Solution:
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        total = [1,2,3,1]
        for i in range(4,n+1):
            if int((i+1) ** 0.5) ** 2 == (i+1):
                total.append(1)
                continue 
            curr = float('inf')
            l = 0
            r = i-1
            while r >= l:
                curr = min(curr,total[l]+total[r])
                r -= 1
                l += 1
            total.append(curr)
        return total[n-1] 