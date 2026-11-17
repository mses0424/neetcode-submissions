class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sub = []
        total = [i for i in range(1,n+1)]
        def dfs(i, k):
            if k == 0:
                res.append(sub[:])
                return
            if i >= n:
                return
            dfs(i+1,k)

            sub.append(total[i])
            dfs(i+1,k-1)
            sub.pop()
        dfs(0,k)
        return res