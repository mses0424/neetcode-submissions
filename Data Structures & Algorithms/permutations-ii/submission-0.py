class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        total = [False] * len(nums)
        res = []
        sub = []
        def dfs():
            if len(sub) == len(nums):
                if sub not in res:
                    res.append(sub[:])
                return
            for i in range(len(nums)):
                if not total[i]:
                    sub.append(nums[i])
                    total[i] = True
                    dfs()
                    total[i] = False
                    sub.pop()
        dfs()
        return res