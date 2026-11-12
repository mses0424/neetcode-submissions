class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or int(s[0]) == 0:
            return 0
        total = [1,1]
        for i in range(1,len(s)):
            count = 0
            if int(s[i]) == 0:
                if int(s[i-1]) >= 3 or int(s[i-1]) == 0:
                    return 0
                else:
                    count += total[i-1]
            elif int(s[i]) <= 6:
                count += total[i]
                if int(s[i-1]) <= 2 and int(s[i-1]) != 0:
                    count += total[i-1]
            else:
                count += total[i]
                if int(s[i-1]) == 1:
                    count += total[i-1]
            total.append(count)
        print(total)
        return total[len(s)]
            
