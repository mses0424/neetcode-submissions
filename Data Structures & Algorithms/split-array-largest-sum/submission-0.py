class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        start = max(nums)
        end = sum(nums)
        while start < end:
            mid = (start + end) // 2
            need = 1
            curr = 0
            for item in nums:
                if curr + item > mid:
                    need += 1
                    curr =0
                curr += item
            if need > k:
                start = mid + 1
            else:
                end = mid
        return start
