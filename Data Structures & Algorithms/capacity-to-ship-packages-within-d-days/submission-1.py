class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start = max(weights)
        end = sum(weights)
        while start < end:
            mid = (start+end) // 2
            curr = 0
            need = 1
            for w in weights:
                if curr + w > mid:
                    need += 1
                    curr = 0
                curr += w
            if need <= days:
                end = mid 
            else:
                start = mid + 1
        return start