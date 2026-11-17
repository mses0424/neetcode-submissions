class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        total = [False] * len(nums)
        def dfs():
            if len(sub) == len(nums):
                res.append(sub[:])
                return
            for i in range(len(nums)):
                if not total[i]:
                    sub.append(nums[i])
                    total[i] = True
                    dfs()
                    sub.pop()
                    total[i] = False
        dfs()
        return res