class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        total = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            total[i][0] = i
        for j in range(n+1):
            total[0][j] = j
        for k in range(1,m+1):
            for l in range(1,n+1):
                if word1[k-1] == word2[l-1]:
                    total[k][l] = total[k-1][l-1]
                else:
                    total[k][l] = min(1+total[k-1][l],1+total[k-1][l-1],1+total[k][l-1])
        return total[m][n]
        