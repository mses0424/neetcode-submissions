class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        total = []
        ans = 0
        for index, val in enumerate(heights):
            start = index
            while total and total[-1][1] > val:
                a,b = total.pop()
                ans = max(ans,b * (index - a))
                start = a
            total.append((start,val))
        return ans