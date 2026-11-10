class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        ans = []
        heap = []
        time = 0
        i = 0
        n = len(tasks)
        while i < n or heap:
            if not heap and time < sorted_tasks[i][0]:
                time = sorted_tasks[i][0]
            while i < n and sorted_tasks[i][0] <= time:
                heapq.heappush(heap, (sorted_tasks[i][1], sorted_tasks[i][2]))
                i += 1
            proc_time, idx = heapq.heappop(heap)
            time += proc_time
            ans.append(idx)
        return ans