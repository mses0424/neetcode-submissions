class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        total = defaultdict(int)
        for item in nums:
            total[item] += 1
        a = max(nums)
        while k > 1:
            total[a] -= 1
            while total[a] == 0:
                a -= 1
            k -= 1
        return a
