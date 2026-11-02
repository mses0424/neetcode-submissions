class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        for item in range(1,len(nums)):
            if nums[item] != nums[item-1]:
                nums[idx] = nums[item]
                idx += 1
        return idx