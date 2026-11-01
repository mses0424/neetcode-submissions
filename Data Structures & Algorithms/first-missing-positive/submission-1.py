class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in nums:
            while 1 <= i and i <= len(nums) and nums[i-1] != i:
                nums[i-1], i = i, nums[i-1]
        for j in range(0,len(nums)):
            if nums[j] != j+1:
                return j+1
        return len(nums)+1