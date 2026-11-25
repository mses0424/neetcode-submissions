class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        visit = {beginWord}
        now = deque([beginWord])
        depth = 1  
        while now:
            for _ in range(len(now)):
                curr = now.popleft()
                if curr == endWord:
                    return depth
                for i in range(len(curr)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        nxt = curr[:i] + c + curr[i+1:]
                        if nxt in word_set and nxt not in visit:
                            visit.add(nxt)
                            now.append(nxt)    
            depth += 1    
        return 0