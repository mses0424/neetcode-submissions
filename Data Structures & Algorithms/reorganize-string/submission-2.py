class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ""
        total = Counter(s)
        thre = len(s) // 2 if len(s) % 2 == 0 else (len(s) // 2) + 1
        if max(total.values()) > thre:
            return ans
        heap = [(-val,key) for key,val in total.items()]
        cand = []
        heapq.heapify(heap)
        while heap:
            curr = heapq.heappop(heap)
            ans += curr[1]
            if cand:
                a = cand.pop()
                heapq.heappush(heap,a)
            if curr[0] < -1:
                cand.append((curr[0] + 1, curr[1]))
        return ans