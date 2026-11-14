class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []
        
        for i, char in enumerate(s):
            if char == '(':
                left_stack.append(i)
            elif char == '*':
                star_stack.append(i)
            else: # 遇到 ')'
                if left_stack:
                    left_stack.pop() # 優先用 '(' 抵銷
                elif star_stack:
                    star_stack.pop() # 退而求其次用 '*' 抵銷
                else:
                    return False     # 兩者皆空，無法抵銷 ')'
                    
        # 結算：檢查剩下的 '(' 是否都有右邊的 '*' 可以配對
        while left_stack and star_stack:
            # 如果 '(' 的位置在 '*' 的右邊，那這個 '*' 救不了它
            if left_stack[-1] > star_stack[-1]:
                return False
            left_stack.pop()
            star_stack.pop()
            
        # 如果 left_stack 還有剩，代表沒有足夠的 '*' 可以抵銷
        return len(left_stack) == 0