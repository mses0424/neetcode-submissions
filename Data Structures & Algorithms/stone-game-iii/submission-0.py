class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        total = [0] * (len(stoneValue) + 1)
        for i in range(len(stoneValue)-1,-1,-1):
            diff = float('-inf')
            take = 0
            for j in range(3):
                if i + j < len(stoneValue):
                    take += stoneValue[i+j]
                    diff = max(diff, take - total[i+j+1])
            total[i] = diff
        if total[0] > 0:
            return "Alice"
        elif total[0] < 0:
            return "Bob"
        else:
            return "Tie"