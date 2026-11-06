class Solution:
    def isValid(self, s: str) -> bool:
        total = []
        if s[0] == "}" or s[0] == ")" or s[0] == "]":
            return False
        for i in range(len(s)):
            if s[i] == "{" or s[i] == "(" or s[i] == "[":
                total.append(s[i])
            else:
                if s[i] == "}":
                    if len(total) == 0 or total.pop() != "{":
                        return False
                if s[i] == "]":
                    if len(total) == 0 or total.pop() != "[":
                        return False
                if s[i] == ")":
                    if len(total) == 0 or total.pop() != "(":
                        return False
        return True if len(total) == 0 else False