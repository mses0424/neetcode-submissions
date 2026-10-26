class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        Flag = True
        for row in board:
            new = defaultdict(int)
            for count in range(1,10):
                new[count] = 0
            for item in row:
                new[item] += 1
                if item != "." and new[item] >= 2:
                    Flag = False

        for i in range(0,9):
            new = defaultdict(int)
            for count in range(1,10):
                new[count] = 0
            for row in board:
                new[row[i]] += 1
                for item in new:
                    if item != "." and new[item] >= 2:
                        Flag = False
        for i in range(0,9,3):
            for j in range(0,9,3):
                new = defaultdict(int)
                for count in range(1,10):
                    new[count] = 0
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        new[board[k][l]] += 1
                        for item in new:
                            if item != "." and new[item] >= 2:
                                Flag = False
        return Flag
