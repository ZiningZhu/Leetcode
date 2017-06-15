public class Solution {
    private boolean legal(char[][] board, int i, int j, char k) {
        for (int x=0; x<9; x++) {
            if (board[i][x] == k && x!=j) {
                return false;
            }
            if (board[x][j] == k && x!=i) {
                return false;
            }
        }
        int r = (i / 3) * 3;
        int c = (j / 3) * 3;
        for (int x=r; x<r+3; x++) {
            for (int y=c; y<c+3; y++) {
                if (board[x][y] == k && x!=i && y!=j) {
                    return false;
                }
            }
        }
        return true;
    }
    private boolean solve(char[][] board) {
        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                if (board[i][j] == '.') {
                    for (char k='1'; k<='9'; k++) {
                        board[i][j] = k;
                        if (!legal(board, i, j, k)) {
                            board[i][j] = '.';
                        } else {
                            boolean tmp = solve(board);
                            if (!tmp) {
                                board[i][j] = '.';
                            } else {
                                return true;
                            }
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
    public void solveSudoku(char[][] board) {
        // Basic backtracking. Try 1-9 for each empty cell.

        boolean status = solve(board);
        if (status == false) {
            System.out.println("Board unsolvable!");
        }
    }
}
