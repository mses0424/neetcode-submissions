class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        total = defaultdict(list)
        for i in range(0,len(nums)):
            total[nums[i]].append(i+1)
        for values in total.values():
            if len(values) >= 2:
                for i in range(0,len(values)-1):
                    if values[i+1] - values[i] <= k:
                        return True
        return False