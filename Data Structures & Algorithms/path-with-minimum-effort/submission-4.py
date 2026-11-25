class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        graph = [[float("inf")] * col for _ in range(row)]
        direct = [(0,1),(0,-1),(1,0),(-1,0)]
        total = [(0,0,0)]
        graph[0][0] = 0
        while total:
            value, r,c = heapq.heappop(total)
            if c == col-1 and r == row-1:
                return value
            if value > graph[r][c]:
                continue
            for dc, dr in direct:
                nc, nr = dc+c, dr+r
                if 0 <= nc < col and 0 <= nr < row:
                    new = max(value, abs(heights[nr][nc]-heights[r][c]))
                    if new < graph[nr][nc]:
                        graph[nr][nc] = new
                        heapq.heappush(total,(new,nr,nc))
        return 0
                    
