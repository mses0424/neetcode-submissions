class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = nums[0]
        ans = 1
        for i in nums[1:]:
            if i == current:
                nums.remove(i)
            ans += 1
            current = i
        return ans