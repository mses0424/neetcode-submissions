class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        total = defaultdict(list)
        for start, end in tickets:
            heapq.heappush(total[start],end)
        route = []
        def dfs(airport):
            while total[airport]:
                curr = heapq.heappop(total[airport])
                dfs(curr)
            route.append(airport)
        dfs("JFK")
        return route[::-1]