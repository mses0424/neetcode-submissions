class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = [0] * (target+1)
        one = Counter(nums)
        res[0] = 1
        res[1] = one[1]
        for i in range(2,target+1):
            now = 0
            for num in nums:
                if num <= i:
                    now += res[i-num]
            res[i] = now
        return res[target] 
        