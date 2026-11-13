class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        total = [[False] * (n+1) for _ in range(m+1)]
        total[0][0] = True
        for i in range(2,n+1):
            if p[i-1] == "*":
                total[0][i] = total[0][i-2]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] != "*":
                    if p[j-1] == s[i-1] or p[j-1] == ".":
                        total[i][j] = total[i-1][j-1]
                else:
                    total[i][j] = total[i][j-2]
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        total[i][j] = total[i][j] or total[i-1][j]
        return total[m][n]