class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {value : idx for idx, value in enumerate(s)}
        start = 0
        end = 0
        res = []
        for i in range(len(s)):
            end = max(end, last[s[i]])
            if i == end:
                res.append(end-start+1)
                start = i + 1
        return res