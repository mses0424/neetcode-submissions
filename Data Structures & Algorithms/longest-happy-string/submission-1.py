class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        total = {'a':a, 'b':b, 'c':c}
        ans = ""
        heap = [(-val, key) for key, val in total.items()]
        heapq.heapify(heap)
        cand = []
        while heap:
            curr = heapq.heappop(heap)
            if curr[0] == 0:
                continue
            if cand:
                heapq.heappush(heap,cand.pop())
            if not ans or ans[-1] != curr[1]:
                ans += curr[1] 
                if curr[0] < -1:
                    heapq.heappush(heap,(curr[0]+1,curr[1]))
            else:
                ans += curr[1]
                if curr[0] < -1:
                    cand.append((curr[0]+1,curr[1]))
        return ans
