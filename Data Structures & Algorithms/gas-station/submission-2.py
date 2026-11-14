class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_diff = 0 
        curr_gas = 0   
        start_idx = 0   
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_diff += diff
            curr_gas += diff
            if curr_gas < 0:
                start_idx = i + 1
                curr_gas = 0
        if total_diff < 0:
            return -1
        return start_idx