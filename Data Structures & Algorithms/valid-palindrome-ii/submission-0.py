class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for i in range(0,len(s)):
            new = s.replace(s[i],"")
            if new == new[::-1]:
                return True
        return False