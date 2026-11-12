class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = cur_min = cur_max = nums[0]

        for n in nums[1:]:  # 若想連切片空間都省掉，可用 for i in range(1, len(nums)):
            # 必須先用暫存變數接住新算出的 cur_max，避免更新 cur_min 時用到被覆蓋的新值
            temp_max = max(n, n * cur_max, n * cur_min)
            cur_min = min(n, n * cur_max, n * cur_min)
            cur_max = temp_max

            res = max(res, cur_max)

        return res