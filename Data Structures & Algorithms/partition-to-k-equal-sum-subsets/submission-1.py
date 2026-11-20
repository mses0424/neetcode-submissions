class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        subset = [0] * k
        def backtrack(i):
            if i == len(nums):
                return True
            for j in range(k):
                if subset[j] + nums[i] > target:
                    continue
                if j > 0 and subset[j-1] == subset[j]:
                    continue
                subset[j] += nums[i]
                if backtrack(i+1):
                    return True
                subset[j] -= nums[i]
            return False
        return backtrack(0)
