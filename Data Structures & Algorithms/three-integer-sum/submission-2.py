class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = nums.sort()
        ans = []
        for i in range(len(nums)):
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    if not [nums[i],nums[l],nums[r]] in ans:
                        ans.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        
        return ans
