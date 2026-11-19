class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        total = set()

        def backtrack(i: int, row: int, column: int) -> bool:
            if i == len(word):
                return True
            if (not (0 <= row < rows) or 
                not (0 <= column < cols) or 
                (row, column) in total or 
                board[row][column] != word[i]):
                return False
            total.add((row, column))
            found = (backtrack(i + 1, row + 1, column) or
                     backtrack(i + 1, row, column + 1) or
                     backtrack(i + 1, row - 1, column) or
                     backtrack(i + 1, row, column - 1))
            total.remove((row, column))
            return found
        for r in range(rows):
            for c in range(cols):
                if backtrack(0, r, c):
                    return True 
        return False