class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # 選擇 1：忽略 s[left]，檢查 s[left+1...right]
                skip_left = s[left + 1 : right + 1]
                # 選擇 2：忽略 s[right]，檢查 s[left...right-1]
                skip_right = s[left : right]
                
                # 只要其中一個是迴文即可
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            
            left += 1
            right -= 1
            
        return True