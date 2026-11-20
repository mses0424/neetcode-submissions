from typing import List
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        target = total // 4
        matchsticks.sort(reverse=True)
        if matchsticks[0] > target:
            return False
        sides = [0, 0, 0, 0]
        def backtrack(i: int) -> bool:
            if i == len(matchsticks):
                return True  
            for j in range(4):
                if sides[j] + matchsticks[i] > target:
                    continue
                # if j > 0 and sides[j] == sides[j - 1]:
                #     continue
                sides[j] += matchsticks[i]
                if backtrack(i + 1):
                    return True
                sides[j] -= matchsticks[i]
            return False
        return backtrack(0)