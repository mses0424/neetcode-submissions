class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)
        for item in s1:
            s1_count[item] += 1
        for item in range(0,len(s1)):
            s2_count[s2[item]] += 1
            flag = True
            for key in s1_count:
                if s2_count[key] != s1_count[key]:
                    flag = False
                    continue
            if flag:
                return True
        for i in range(1,len(s2)-len(s1)+1):
            s2_count[s2[i-1]] -= 1
            s2_count[s2[i+len(s1)-1]] += 1
            flag = True
            for key in s2_count:
                if s2_count[key] != s1_count[key]:
                    flag = False
                    continue
            if flag:
                return True
        return False