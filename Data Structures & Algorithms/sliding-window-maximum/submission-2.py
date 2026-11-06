class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        current = deque()
        for i in range(len(nums)):
            while current and nums[current[-1]] <= nums[i]:
                current.pop()
            if current and i - current[0] >= k:
                current.popleft()
            current.append(i)
            if i - k + 1 >= 0:
                ans.append(nums[current[0]])
        return ans
