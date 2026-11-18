class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # res = [[]]
        # nums.sort()
        # for num in nums:
        #     curr = []
        #     for item in res:
        #         curr.append(item + [num])
        #         if (item + [num]) in res:
        #             curr.pop()
        #     res.extend(curr)
        # return res
        nums.sort()  # 先排序，讓重複的數字靠在一起
        res = [[]]
        prev_size = 0  # 紀錄上一輪擴充前的 res 長度
        
        for i in range(len(nums)):
            # 如果目前的數字跟前一個數字一樣，我們就從上一輪新增的起點開始擴充
            # 如果不一樣，我們就從頭 (index 0) 開始擴充
            start_index = prev_size if i > 0 and nums[i] == nums[i - 1] else 0
            
            # 更新 prev_size 為目前的 res 長度，給下一回合參考
            prev_size = len(res)
            
            # 只針對需要擴充的部分進行合併
            for j in range(start_index, prev_size):
                res.append(res[j] + [nums[i]])

        return res