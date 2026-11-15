class Solution:
    def search(self, nums: List[int], target: int) -> int:
        end = len(nums)-1
        start = 0
        while start < end:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                return mid
        if nums[start] == target:
            return start
        else:
            return -1