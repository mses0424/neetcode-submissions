class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        now = 0
        heap = []
        new = sorted([(item[1],item[2],item[0]) for item in trips])
        for item in new:
            while heap:
                if heap[0][0] <= item[0]:
                    now -= heap[0][1]
                    heapq.heappop(heap)
                else:
                    break
            now += item[2]
            heapq.heappush(heap,(item[1],item[2]))
            if now > capacity:
                return False
        return True