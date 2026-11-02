class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        front = height[0]
        end = height[len(height)-1]
        big = height[0]
        idx = 0
        for i in range(1,len(height)):
            if height[i] > big:
                big = height[i]
                idx = i
        for j in range(1,idx):
            if height[j] > front:
                front = height[j]
            else:
                ans += front - height[j]
        for k in range(len(height)-1,idx,-1):
            if height[k] > end:
                end = height[k]
            else:
                ans += end - height[k]
        return ans
