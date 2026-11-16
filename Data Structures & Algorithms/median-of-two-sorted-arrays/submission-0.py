class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        m = len(num1)
        n = len(num2)
        target = (m + n + 1) // 2
        start = 0
        end = m
        while start < end:
            mid = (start + end) // 2
            pick = target - mid
            if num1[mid] < num2[pick-1]:
                start = mid + 1
            else:
                end = mid
        first = start
        second = target - first
        i = num1[first-1] if first != 0 else float('-inf')
        j = num2[second-1] if second != 0 else float('-inf')  
        left = max(i,j)
        if (m + n) % 2 == 1:
            return float(left)
        k = num1[first] if first != len(num1) else float('inf')
        l = num2[second] if second != len(num2) else float('inf') 
        right = min(k,l)
        return (left + right) / 2 