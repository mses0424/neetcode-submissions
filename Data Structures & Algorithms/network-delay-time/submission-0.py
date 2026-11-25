class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for item in times:
            graph[item[0]].append((item[1],item[2]))
        dist = [float("inf")] * n
        dist[k-1] = 0
        curr = [(0,k)]
        while curr:
            value, point = heapq.heappop(curr)
            if value > dist[point-1]:
                continue
            for item in graph[point]:
                if item[1]+value < dist[item[0]-1]:
                    dist[item[0]-1] = item[1] + value
                    curr.append((item[1]+value,item[0]))
        ans = -1
        print(dist)
        for i in range(n):
            if dist[i] == float("inf"):
                return -1
            else:
                ans = max(ans,dist[i])
        return ans