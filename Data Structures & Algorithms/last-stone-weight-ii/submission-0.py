class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        res = [False] * (target + 1)
        res[0] = True
        for item in stones:
            if item <= target:
                for i in range(target, item-1, -1):
                    if res[i-item]:
                        res[i] = True
        for j in range(target,-1,-1):
            if res[j] == True:
                return total - j * 2
                