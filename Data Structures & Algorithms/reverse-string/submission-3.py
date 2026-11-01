class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        idx = n // 2
        for i in range(0,idx):
            s[i], s[n-i-1] = s[n-i-1], s[i]