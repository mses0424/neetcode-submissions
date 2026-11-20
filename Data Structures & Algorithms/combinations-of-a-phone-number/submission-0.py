from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []
        curr = []  
        def backtrack(i: int):
            if i == len(digits):
                res.append("".join(curr))
                return
            for char in phone_map[digits[i]]:
                curr.append(char)  
                backtrack(i + 1)      
                curr.pop()   
        backtrack(0)
        return res