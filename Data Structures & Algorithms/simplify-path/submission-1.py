class Solution:
    def simplifyPath(self, path: str) -> str:
        total = []
        stack = []
        ans = "/"
        current = ""
        for i in range(len(path)):
            if path[i] != "/":
                current += path[i]
            elif path[i] == "/":
                if len(current) > 0:
                    total.append(current)
                    current = ""
        if len(current) > 0:
            total.append(current)
        for i in range(len(total)):
            if total[i] == "..":
                if len(stack) > 0:
                    stack.pop()
            elif total[i] != ".":
                stack.append(total[i])
        if stack:
            for i in range(len(stack)):
                if i != len(stack) - 1:
                    ans += stack[i] + "/"
                else:
                    ans += stack[i]
        return ans