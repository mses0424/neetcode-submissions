class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        total = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    total[i] = max(total[i],total[j]+1)
        return max(total)