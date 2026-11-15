class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0]) - 1
        start = 0
        while start < m:
            mid = (start + m) // 2
            if matrix[mid][0] < target:
                start = mid + 1
            elif matrix[mid][0] > target:
                m = mid
            else:
                return True
        print(start-1)
        row = start - 1
        start = 0
        while start < n:
            mid = (start + n) // 2
            if matrix[row][mid] < target:
                start = mid + 1
            elif matrix[row][mid] > target:
                n = mid - 1
            else:
                return True
        print(start)
        return True if matrix[row][start] == target else False
        
