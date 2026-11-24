class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (start, fin), value in zip(equations,values):
            graph[start].append((fin,value))
            graph[fin].append((start,1.0 / value))
        def bfs(start,finish):
            if not start in graph or not finish in graph:
                return -1.0
            if start == finish:
                return 1.0
            visit = set(start)
            now = deque()
            now.append((start,1.0))
            while now:
                curr, value = now.popleft()
                if curr == finish:
                    return value
                for nxt, val in graph[curr]:
                    if nxt not in visit:
                        visit.add(nxt)
                        now.append((nxt,val*value))
            return -1.0
        return [bfs(c,d) for (c,d) in queries]