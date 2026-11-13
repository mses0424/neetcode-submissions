from typing import List
from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 在頭尾加入虛擬氣球 1
        nums = [1] + nums + [1]
        
        @cache
        def dfs(left: int, right: int) -> int:
            # 邊界條件：如果開區間 (left, right) 內沒有氣球了
            if left + 1 == right:
                return 0
                
            max_coins = 0
            # 枚舉區間內哪一顆氣球 k 是「最後」被戳破的
            for k in range(left + 1, right):
                # k 破掉得到的分數：nums[left] * nums[k] * nums[right]
                # 加上左半區間的最大分數 dfs(left, k)
                # 加上右半區間的最大分數 dfs(k, right)
                coins = dfs(left, k) + (nums[left] * nums[k] * nums[right]) + dfs(k, right)
                max_coins = max(max_coins, coins)
                
            return max_coins
            
        # 求戳破 (0, len(nums)-1) 之間所有氣球的最大分數
        return dfs(0, len(nums) - 1)