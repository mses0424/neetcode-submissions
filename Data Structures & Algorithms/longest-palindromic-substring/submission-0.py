class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_len = 0
        res_start = 0
        def expand(l, r):
            nonlocal res_len, res_start
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    res_len = r - l + 1
                    res_start = l
                l -= 1
                r += 1
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)
        return s[res_start:res_start + res_len]