class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        total = Counter(tasks)
        heap = [-cnt for cnt in total.values()]
        heapq.heapify(heap)
        wait = deque()
        time = 0
        while heap or wait:
            time += 1
            if heap:
                a = heapq.heappop(heap)
                a += 1
                if a != 0:
                    wait_time = time + n
                    wait.append((a,wait_time))
            if wait:
                if wait[0][1] == time:
                    heapq.heappush(heap,wait[0][0])
                    wait.popleft()
        return time

