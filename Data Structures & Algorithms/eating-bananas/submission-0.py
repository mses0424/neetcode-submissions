class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        while start < end:
            mid = (start+end) // 2
            curr = sum(((pile+mid-1) // mid) for pile in piles)
            if curr <= h:
                end = mid
            elif curr > h:
                start = mid + 1
        return start