class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        total = []
        if not nums:
            return 0
        total.append((nums[0],nums[0]))
        for i in range(1,len(nums)):
            big = max(nums[i],nums[i]*total[i-1][0],nums[i]*total[i-1][1])
            small = min(nums[i],nums[i]*total[i-1][0],nums[i]*total[i-1][1])
            total.append((small,big))
        return max(item[1] for item in total)
