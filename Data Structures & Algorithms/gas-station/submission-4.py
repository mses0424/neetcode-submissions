from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 直接用底層 C 優化的 sum() 秒殺無解的情況
        if sum(gas) < sum(cost):
            return -1
            
        curr_gas = 0
        start_idx = 0
        
        for i in range(len(gas)):
            curr_gas += gas[i] - cost[i]
            
            # 如果油箱變負的，下一個站點當新起點
            if curr_gas < 0:
                start_idx = i + 1
                curr_gas = 0
                
        return start_idx