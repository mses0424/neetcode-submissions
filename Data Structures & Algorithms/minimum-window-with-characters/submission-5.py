class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        total_t = defaultdict(int)
        total_s = defaultdict(int)
        for item in t:
            total_t[item] += 1
        need = len(total_t)
        have = 0
        start = 0
        ans_len = len(s) + 1
        ans_start = 0
        for i in range(len(s)):
            total_s[s[i]] += 1
            if s[i] in total_t and total_s[s[i]] == total_t[s[i]]:
                have += 1
            while have == need:
                if ans_len > i - start + 1:
                    ans_len = i - start + 1
                    ans_start =  start
                total_s[s[start]] -= 1
                if total_s[s[start]] < total_t[s[start]]:
                    have -= 1
                start += 1
        return s[ans_start:ans_start+ans_len] if ans_len != len(s) + 1 else ""
