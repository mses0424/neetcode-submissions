class Solution:
    def jump(self, nums: List[int]) -> int:
        total = [float('inf')] * len(nums)
        if nums[0] == 0:
            return 0
        total[0] = 0
        for i in range(len(nums)):
            for j in range(i+1,i+nums[i]+1):
                if j < len(nums):
                    total[j] = min(total[j], total[i]+1)
        print(total)
        return total[len(nums)-1] if total[len(nums)-1] != float('inf') else 0
