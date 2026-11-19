class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, left, right):
            if len(curr) == n * 2:
                res.append(curr)
                return
            if left < n:
                backtrack(curr+"(", left+1, right)
            if left > right:
                backtrack(curr+")", left, right+1)
        backtrack("",0,0)
        return res