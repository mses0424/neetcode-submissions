class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max = 0
        total_max = nums[0]
        curr_min = 0
        total_min = nums[0]
        total = sum(nums)
        for item in nums:
            curr_max = max(item, curr_max+item)
            total_max = max(total_max, curr_max)
            curr_min = min(item, curr_min+item)
            total_min = min(total_min, curr_min)
        if total_max < 0:
            return total_max
        return max(total_max, total-total_min)
