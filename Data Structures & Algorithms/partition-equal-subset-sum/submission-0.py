class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        res = [False] * (target+1)
        res[0] = True
        for num in nums:
            if num <= target:
                for i in range(target,num-1,-1):
                    if res[i-num]:
                        res[i] = True
        return res[target]

                
            