class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # res = [[]]
        # nums.sort()
        # for num in nums:
        #     curr = []
        #     for item in res:
        #         curr.append(item + [num])
        #         if (item + [num]) in res:
        #             curr.pop()
        #     res.extend(curr)
        # return res
        res = []
        nums.sort()
        sub = []
        def dfs(i):
            if i == len(nums):
                res.append(sub[:])
                return
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
            while i < len(nums)-1 and nums[i+1] == nums[i]:
                i += 1
            dfs(i+1)
        dfs(0)
        return res