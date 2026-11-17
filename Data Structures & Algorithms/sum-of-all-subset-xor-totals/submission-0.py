class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        for item in nums:
            total |= item
        return total << len(nums) - 1