        
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def bfs(starts):
            visit = set(starts)
            queue = deque(starts)
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows and 0 <= nc < cols and
                        (nr, nc) not in visit and
                        heights[nr][nc] >= heights[r][c]  # 往等高或更高的地方爬
                    ):
                        visit.add((nr, nc))
                        queue.append((nr, nc))
            return visit

        pac_starts = [(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)]
        atl_starts = [(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)]

        pac = bfs(pac_starts)
        atl = bfs(atl_starts)

        return [list(cell) for cell in (pac & atl)]