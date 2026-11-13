class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        a = sum(nums)
        if (a + target) % 2 == 1 or a < abs(target):
            return 0
        real = (a + target) // 2
        total = [0] * (real+1)
        total[0] = 1
        for num in nums:
            if num <= real:
                for i in range(real,num-1,-1):
                    total[i] += total[i-num]
        return total[real]
