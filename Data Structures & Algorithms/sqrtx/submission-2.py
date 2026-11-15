class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        start = 0
        end = x+1
        while start < end:
            mid = (start + end) // 2
            if mid ** 2 < x:
                start = mid + 1
            elif mid ** 2 > x:
                end = mid
            else:
                return mid
        return start - 1