class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        if nums[0] >= len(nums):
            return True
        curr = nums[0]
        for i in range(1,len(nums)):
            for j in range(i,curr+1):
                curr = max(curr, j + nums[j])
            if curr >= (len(nums)-1):
                return True
            if curr <= i:
                return False
        