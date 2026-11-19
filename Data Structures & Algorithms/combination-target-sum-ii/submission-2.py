class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()
        def dfs(i, remain):
            if remain == 0:
                res.append(subset[:])
                return 
            if remain < 0 or i == len(candidates):
                return
            subset.append(candidates[i])
            dfs(i+1, remain-candidates[i])
            subset.pop()
            while len(candidates)-1 > i and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1,remain)
        dfs(0,target)
        return res