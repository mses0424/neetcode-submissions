class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        total = [[0] * n for _ in range(m)]
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(l,r):
            nonlocal directions,m,n
            if total[l][r] > 0:
                return total[l][r]
            local = 1
            for nl,nr in directions:
                dl = l + nl
                dr = r + nr
                if 0 <= dl < m and 0 <= dr < n and matrix[dl][dr] > matrix[l][r]:
                    local = max(local, 1 + dfs(dl,dr))
            total[l][r] = local
            return local
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j))
                
        return ans