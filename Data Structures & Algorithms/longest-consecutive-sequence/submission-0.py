class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        order = set(nums)
        ans = 0
        for item in order:
            if item-1 not in order:
                length = 1
                now = item+1
                while now in order:
                    length += 1
                    now += 1
                ans = max(ans,length)
        return ans