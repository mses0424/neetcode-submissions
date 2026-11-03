class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        start = 0
        ans = 0
        for item in s:
            i = 0
            l = len(a)
            a.add(ord(item))
            while l == len(a) + i and len(a) > 1:
                a.remove(ord(s[start]))
                a.add(ord(item))
                start += 1
                i += 1
            ans = max(ans,len(a))
        return ans