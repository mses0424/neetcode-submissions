class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        total = Counter(tasks)
        high = max(total.values())
        high_freq = sum(1 for i in total.values() if i == high)
        return max(len(tasks),(high-1) * (n+1) + high_freq)