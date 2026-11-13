class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        total = [[False] * (n+1) for _ in range(m+1)]
        for i in range(n+1):
            if s2[:i] == s3[:i]:
                total[0][i] = True
            else:
                total[0][i] = False
        for j in range(m+1):
            if s1[:j] == s3[:j]:
                total[j][0] = True
            else:
                total[j][0] = False
        for k in range(1,m+1):
            for l in range(1,n+1):
                leng = k + l
                total[k][l] = (total[k-1][l] and s1[k-1] == s3[leng-1]) or (total[k][l-1] and s2[l-1] == s3[leng-1])
        return total[m][n]