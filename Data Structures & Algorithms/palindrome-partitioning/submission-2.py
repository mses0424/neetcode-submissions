class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def decide(s):
            if s == s[::-1]:
                return True
            return False
        res = []
        curr = []
        def backtrack(i,start):
            if i == len(s):
                res.append(curr[:])
                return
            if i < len(s) - 1:
                backtrack(i+1,start)
            if decide(s[start:i+1]):
                curr.append(s[start:i+1])
                backtrack(i+1,i+1)
                curr.pop()
        backtrack(0,0)
        return res

