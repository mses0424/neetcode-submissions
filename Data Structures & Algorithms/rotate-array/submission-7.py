class Solution:

    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # 1. 翻轉整個陣列
        reverse(0, n - 1)
        # 2. 翻轉前 k 個元素
        reverse(0, k - 1)
        # 3. 翻轉剩下的 n - k 個元素
        reverse(k, n - 1)