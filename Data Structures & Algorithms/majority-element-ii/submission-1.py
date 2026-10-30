class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        thre = len(nums) // 3
        total = defaultdict(int)
        ans = []
        for item in nums:
            total[item] += 1
        for item in total:
            if total[item] > thre:
                ans.append(item)
        return ans