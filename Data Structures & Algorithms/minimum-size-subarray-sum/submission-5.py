class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        current = 0
        ans = len(nums)
        if sum(nums) < target:
            return 0
        for i in range(len(nums)):
            current += nums[i]
            while current >= target:
                ans = min(ans,i-start+1)
                current -= nums[start]
                start += 1
        return ans