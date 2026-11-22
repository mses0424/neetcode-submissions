        
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()
        def dfs(i,j,oce,prev):
            if not 0 <= i < rows or not 0 <= j < cols or (i,j) in oce or heights[i][j] < prev:
                return 
            oce.add((i,j))
            dfs(i+1,j,oce,heights[i][j]) 
            dfs(i-1,j,oce,heights[i][j]) 
            dfs(i,j+1,oce,heights[i][j]) 
            dfs(i,j-1,oce,heights[i][j]) 
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        return [list(item) for item in pac & atl]