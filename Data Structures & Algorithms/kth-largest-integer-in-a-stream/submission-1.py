class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        i = 0
        while i < len(self.nums) and val > self.nums[i]:
            i += 1
        self.nums.insert(i,val)
        return self.nums[-self.k]

        
