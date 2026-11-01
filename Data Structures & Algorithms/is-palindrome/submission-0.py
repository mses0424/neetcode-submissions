class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = [item.lower() for item in s if item.isalnum()]
        return new == new[::-1]