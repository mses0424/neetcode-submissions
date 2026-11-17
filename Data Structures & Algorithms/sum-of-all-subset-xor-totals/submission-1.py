class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index, current_xor):
            # 走到陣列盡頭，回傳當前子集合的 XOR 總和
            if index == len(nums):
                return current_xor
            
            # 選擇 1：不把 nums[index] 加入子集合
            without_current = dfs(index + 1, current_xor)
            
            # 選擇 2：把 nums[index] 加入子集合 (進行 XOR 運算)
            with_current = dfs(index + 1, current_xor ^ nums[index])
            
            # 將兩條分支的結果加總
            return without_current + with_current
            
        return dfs(0, 0)