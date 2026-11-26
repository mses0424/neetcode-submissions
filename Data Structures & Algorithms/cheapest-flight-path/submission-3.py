class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        depth = [float("inf")] * n
        depth[src] = 0
        for _ in range(k+1):
            tmp_depth = depth.copy()
            for start, end, dist in flights:
                if depth[start] != float("inf") and depth[start] + dist < tmp_depth[end]:
                    tmp_depth[end] = depth[start] + dist
            depth = tmp_depth
        return -1 if depth[dst] == float("inf") else depth[dst]