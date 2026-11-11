class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        now = deque(sorted(zip(capital,profits)))
        ava = []
        if now[0][0] > w:
            return w
        while k:
            while now and now[0][0] <= w:
                heapq.heappush(ava,(-now[0][1],now[0][0]))
                now.popleft()
            pro, _ = heapq.heappop(ava)
            w += (-pro)
            k -= 1
        return w