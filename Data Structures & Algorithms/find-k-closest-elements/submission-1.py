class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        start = 0
        for i in range(len(arr)):
            if len(ans) <= k:
                ans.append(arr[i])
            if len(ans) > k:
                if abs(x-arr[start]) > abs(x-arr[i]):
                    start += 1
                    ans.pop(0)
                else:
                    ans.pop(k)
        return ans