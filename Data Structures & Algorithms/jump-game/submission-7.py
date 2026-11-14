class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_len = 0
        for i in range(len(nums)):
            if i > max_len:
                return False
            max_len = max(max_len, i + nums[i])
            if max_len >= len(nums):
                return True
        return True
        