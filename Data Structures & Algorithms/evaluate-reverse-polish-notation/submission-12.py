class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = []
        if len(tokens) == 1:
            return int(tokens[0])
        for i in range(len(tokens)):
            if tokens[i] == "+":
                a = int(total.pop())
                b = int(total.pop())
                total.append(a+b)
            elif tokens[i] == "-":
                a = int(total.pop())
                b = int(total.pop())
                total.append(b-a)
            elif tokens[i] == "/":
                a = int(total.pop())
                b = int(total.pop())
                if a * b >= 0:
                    total.append(b//a)
                else:
                    a = abs(a)
                    b = abs(b)
                    total.append(-(b//a))
            elif tokens[i] == "*":
                a = int(total.pop())
                b = int(total.pop())
                total.append(a*b)
            else:
                total.append(tokens[i])
        return total[0]