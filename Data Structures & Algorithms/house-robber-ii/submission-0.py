class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        def rob_linear(num):
            total = []
            if not num:
                return 0
            if len(num) <= 2:
                return max(num)
            a = max(num[0:2])
            total.append(num[0])
            total.append(a)
            for i in range(2,len(num)):
                total.append(max(total[i-1],total[i-2]+num[i]))
            return total[len(num)-1]
        return max(rob_linear(nums[:-1]),rob_linear(nums[1:]))