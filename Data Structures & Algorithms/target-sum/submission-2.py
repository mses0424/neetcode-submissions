from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # dp[sum] = count
        dp = defaultdict(int)
        dp[0] = 1
        
        for num in nums:
            next_dp = defaultdict(int)
            # 遍歷上一輪所有可能的總和
            for current_sum, count in dp.items():
                # 分支 1：加上當前數字
                next_dp[current_sum + num] += count
                # 分支 2：減去當前數字
                next_dp[current_sum - num] += count
            
            # 滾動更新狀態
            dp = next_dp
            
        return dp[target]