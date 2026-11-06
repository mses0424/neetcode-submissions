class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        big = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if len(big) == 0:
                big.append((temperatures[i],i))
                continue
            while temperatures[i] > big[-1][0]:
                a, b = big.pop()
                ans[b] = i - b
                if len(big) == 0:
                    break
            big.append((temperatures[i],i))
        return ans
