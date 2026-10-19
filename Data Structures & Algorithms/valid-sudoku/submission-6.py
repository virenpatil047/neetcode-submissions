class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            mp = defaultdict(int)
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                if not mp[board[i][j]]:
                    mp[board[i][j]] = 1
                else:
                    print(f"row{i}{j} : {mp}")
                    return False
            mp = defaultdict(int)
            for j in range(len(board[i])):
                if board[j][i] == ".":
                    continue
                if not mp[board[j][i]]:
                    mp[board[j][i]] = 1
                else:
                    print(f"col{j}{i} : {mp}")
                    return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                mp = defaultdict(int)
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] == ".":
                            continue
                        if mp[board[r][c]]:
                            return False
                        mp[board[r][c]] = 1
        return True
                    
                