class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_counts = {0: 1}  # 處理 Prefix Sum 剛好等於 k 的情況
        
        for num in nums:
            current_sum += num  # O(1): 更新當前前綴和 P[j]
            
            # O(1): 檢查過去有沒有出現過 P[j] - k
            if current_sum - k in prefix_counts:
                count += prefix_counts[current_sum - k]
            
            # O(1): 記錄當前的 P[j]，供未來的元素使用
            prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
            
        return count