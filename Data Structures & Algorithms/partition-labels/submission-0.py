class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 1:
            return [1]
        res = []
        total = Counter(s)
        now = defaultdict(int)
        now[s[0]] = 1
        have = deque([s[0]])
        start = 1
        while start < len(s) or have:
            if have:
                tar = have.popleft()
                while now[tar] != total[tar]:
                    now[s[start]] += 1
                    if s[start] not in have:
                        have.append(s[start])
                    start += 1
            else:
                if not res:
                    res.append(start)
                else:
                    res.append(start-sum(res))
                have.append(s[start])
        res.append(len(s)- sum(res))
        return res