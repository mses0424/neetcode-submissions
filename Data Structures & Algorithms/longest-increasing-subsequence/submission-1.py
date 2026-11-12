from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            # 找到 tails 中第一個 >= num 的索引位置
            idx = bisect_left(tails, num)
            
            if idx == len(tails):
                # num 比目前所有結尾都大，直接延長最長序列
                tails.append(num)
            else:
                # 替換成更小的結尾，提升未來延長的潛力
                tails[idx] = num

        return len(tails)