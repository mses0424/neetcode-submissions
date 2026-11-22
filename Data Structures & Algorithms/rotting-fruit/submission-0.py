class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    total.append((i,j))
        direction = {(1,0),(-1,0),(0,1),(0,-1)}
        minute = 0
        while fresh > 0:
            times = len(total)
            if times == 0:
                return -1
            print(total,fresh)
            minute += 1
            for _ in range(times):
                r, c = total.popleft()
                for nr, nc in direction:
                    dr = r + nr
                    dc = c + nc
                    if 0 <= dr < len(grid) and 0 <= dc < len(grid[0]) and grid[dr][dc] == 1:
                        total.append((dr,dc))
                        grid[dr][dc] = -1
                        fresh -= 1
        return minute