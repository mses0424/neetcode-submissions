class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        total = cost[0:2]
        for i in range(2,len(cost)):
            total.append(cost[i]+min(total[i-1],total[i-2]))
        return min(total[len(cost)-1],total[len(cost)-2])
