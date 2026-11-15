from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        start = 0
        end = rows * cols - 1
        
        while start < end:
            mid = (start + end) // 2
            val = matrix[mid // cols][mid % cols]  # 一維索引轉二維座標
            if val < target:
                start = mid + 1
            elif val > target:
                end = mid - 1
            else:
                return True
                
        return matrix[start // cols][start % cols] == target