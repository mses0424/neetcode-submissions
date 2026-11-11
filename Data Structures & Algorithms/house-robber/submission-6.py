class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        a = max(nums[:2])
        total = [nums[0]] + [a]
        for i in range(2,len(nums)):
            total.append(max(total[i-1],total[i-2]+nums[i]))
        return total[-1]