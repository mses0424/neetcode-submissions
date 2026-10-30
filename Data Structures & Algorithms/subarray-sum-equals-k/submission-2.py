class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = defaultdict(int)
        ans = 0 
        total[0] = 1
        sum_total = 0
        for item in nums:
            sum_total += item
            if sum_total - k in total:
                ans += total[sum_total - k]
            total[sum_total] += 1
        return ans

