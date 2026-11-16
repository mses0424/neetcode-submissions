from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        start = 1
        end = len(nums) - 1  # 數值範圍 [1, n]

        while start < end:
            mid = (start + end) // 2
            # 統計陣列中有多少個數字 <= mid
            count = sum(num <= mid for num in nums)

            if count <= mid:
                start = mid + 1  # <= mid 的數字沒有超標，重複值一定在右半邊 [mid + 1, end]
            else:
                end = mid        # <= mid 的數字超過 mid 個，保留 mid 並往左半邊縮小範圍

        return start