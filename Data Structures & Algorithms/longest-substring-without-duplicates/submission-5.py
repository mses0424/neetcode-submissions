class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    char_set = set()
    start = 0
    ans = 0
    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        ans = max(ans, end - start + 1)
    return ans