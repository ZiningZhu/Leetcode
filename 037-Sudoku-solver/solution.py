from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        sol = self.solveHelperDFS(board)
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = sol[i][j]
        
        
    def findCandidates(self, board, i, j):
        candidates = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        for k in board[i]:
            if k != "." and k in candidates:
                candidates.remove(k)
        if len(candidates) == 0: return []
        for k in [row[j] for row in board]:
            if k != "." and k in candidates:
                candidates.remove(k)
        if len(candidates) == 0: return []
        for i_ in range(i//3*3, i//3*3+3):
            for j_ in range(j//3*3, j//3*3+3):
                k = board[i_][j_]
                if k != "." and k in candidates:
                    candidates.remove(k)
        return candidates
            
        
    def solveHelperDFS(self, board, layer=0):
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x == ".":
                    cs = self.findCandidates(board, i, j)
                    if len(cs) == 0:
                        return None
                    for c in cs:
                        board[i][j] = c
                        sol = self.solveHelperDFS(board, layer+1)
                        if sol is not None:
                            return sol
                        board[i][j] = "."
                    return None 
        return board


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    filled_board = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]
    sol.solveSudoku(board)
    assert board == filled_board, "Got {} instead.".format(board)

    #print(sol.findCandidates(board, 0,2))