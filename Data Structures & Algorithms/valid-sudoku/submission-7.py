class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col, row, box = defaultdict(list), defaultdict(list), defaultdict(list)
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if val in row[i] or val in col[j] or val in box[(i//3, j//3)]:
                    return False
                row[i].append(val)
                col[j].append(val)
                box[(i//3, j//3)].append(val)
        return True
                    
                