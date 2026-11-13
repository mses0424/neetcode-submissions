class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        total = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            total[i][0] = 1
        for k in range(1,len(s)+1):
            for l in range(1,len(t)+1):
                if s[k-1] == t[l-1]:
                    total[k][l] += total[k-1][l-1]        
                    total[k][l] += total[k-1][l]
                else:
                    total[k][l] += total[k-1][l]
        return total[len(s)][len(t)]