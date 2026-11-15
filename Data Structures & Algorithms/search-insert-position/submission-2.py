class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        end = len(nums)
        start = 0
        while start < end:
            mid = (start+end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        return start 
