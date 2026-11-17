class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i, remain):
            if remain == 0:
                res.append(subset[:])
                return 
            if remain < 0 or i == len(nums):
                return
            subset.append(nums[i]) 
            dfs(i, remain-nums[i])
            subset.pop()

            dfs(i+1,remain)
        dfs(0,target)
        return res