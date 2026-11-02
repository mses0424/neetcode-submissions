class Solution:

    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        # nums[:] 會原地修改原本的列表內容，不會建立新的列表變數
        nums[:] = nums[n - k :] + nums[: n - k]