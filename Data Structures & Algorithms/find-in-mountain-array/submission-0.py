class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        cache = {}
        def get(i: int) -> int:
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]
        start, end = 0, n - 1
        while start < end:
            mid = (start + end) // 2
            if get(mid) < get(mid + 1):
                start = mid + 1
            else:
                end = mid
        peak = start
        start, end = 0, peak
        while start < end:
            mid = (start + end) // 2
            if get(mid) < target:
                start = mid + 1
            else:
                end = mid
        if get(start) == target:
            return start
        start, end = peak + 1, n - 1
        while start < end:
            mid = (start + end) // 2
            if get(mid) > target:
                start = mid + 1 
            else:
                end = mid
        if get(start) == target:
            return start
        return -1