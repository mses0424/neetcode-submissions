class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        total = 0
        start = 0
        ans = 0
        for i in range(len(s)):
            count[s[i]] += 1
            total = max(total,count[s[i]])
            while (i-start+1) - total > k:
                count[s[start]] -= 1
                start += 1
            ans = max(ans,i-start+1)
        return ans
