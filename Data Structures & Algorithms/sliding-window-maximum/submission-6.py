class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # ans = []
        # current = deque()
        # for i in range(len(nums)):
        #     while current and nums[current[-1]] <= nums[i]:
        #         current.pop()
        #     if current and i - current[0] >= k:
        #         current.popleft()
        #     current.append(i)
        #     if i - k + 1 >= 0:
        #         ans.append(nums[current[0]])
        # return ans
        ans = []
        heap = [(-nums[i],i) for i in range(k)]
        heapq.heapify(heap)
        ans.append(-heap[0][0])
        for i in range(k,len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
        return ans