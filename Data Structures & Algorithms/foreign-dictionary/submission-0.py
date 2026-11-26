class Solution:
    def foreignDictionary(self, words: list[str]) -> str:
        adj = {c: set() for word in words for c in word}
        in_degree = {c: 0 for c in adj}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break 
        queue = deque([c for c, deg in in_degree.items() if deg == 0])
        result = []
        while queue:
            curr = queue.popleft()
            result.append(curr)
            for nxt in adj[curr]:
                in_degree[nxt] -= 1
                if in_degree[nxt] == 0:
                    queue.append(nxt)
        if len(result) < len(in_degree):
            return ""    
        return "".join(result)