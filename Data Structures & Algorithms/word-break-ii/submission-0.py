class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        res = []
        curr = []
        def backtrack(start: int):
            if start == len(s):
                res.append(" ".join(curr))
                return
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    curr.append(word)      
                    backtrack(end)         
                    curr.pop()            
        backtrack(0)
        return res