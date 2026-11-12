class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        total = [False] * (len(s) + 1)
        total[0] = True
        for i in range(1,len(s)+1):
            for w in wordDict:
                now = len(w)
                if now <= i and total[i-now] and s[i-now:i] == w:
                    total[i] = True
                    break
        return total[len(s)]