class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ans = 0
        adj = [[] for _ in range(n)]
        walk = [False] * n
        for item in edges:
            adj[item[0]].append(item[1])
            adj[item[1]].append(item[0])
        curr = deque()
        for i in range(n):
            if not walk[i]:
                ans += 1
                curr.append(i)
                while curr:
                    now = curr.popleft()
                    walk[now] = True
                    for j in adj[now]:
                        if walk[j] == False:
                            curr.append(j)
        return ans


