class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for i in range(len(operations)):
            if len(ans) > 0 and operations[i] == 'C':
                ans.pop()
            elif len(ans) > 0 and operations[i] == 'D':
                ans.append(ans[-1]*2)
            elif len(ans) > 0 and operations[i] == '+':
                a = ans[-1]
                b = ans[-2]
                ans.append(a+b)
            else:
                ans.append(int(operations[i]))
        return sum(ans)