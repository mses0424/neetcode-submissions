class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        def expand(l, r):
            nonlocal total
            while l >= 0 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)
        return total