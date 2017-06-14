public class Solution {

    private boolean hasDuplicate(char[] tmp) {
        HashSet<Character> dic = new HashSet<Character>();
        for (int i=0; i < 9; i++) {
            if (tmp[i] == '.') continue;
            if (!dic.add(tmp[i])) {
                return true;
            }
        }
        return false;
    }
    public boolean isValidSudoku(char[][] board) {
        // Validate rows
        for (int i=0; i<9; i++) {
            char[] tmp = new char[9];
            for (int j=0; j<9; j++) {
                tmp[j] = board[i][j];
            }
            if (hasDuplicate(tmp)) {
                return false;
            }
        }

        System.out.println("Row test passed!");
        // Validate columns
        for (int j=0; j<9; j++) {
            char[] tmp = new char[9];
            for (int i=0; i<9; i++) {
                tmp[i] = board[i][j];
            }
            if (hasDuplicate(tmp)) {
                return false;
            }
        }
        System.out.println("Column test passed!");
        // Validate small areas
        for (int i=0; i<9; i=i+3) {
            for (int j=0; j<9; j=j+3) {
                char[] tmp = new char[9];
                tmp[0] = board[i][j];
                tmp[1] = board[i][j+1];
                tmp[2] = board[i][j+2];
                tmp[3] = board[i+1][j];
                tmp[4] = board[i+1][j+1];
                tmp[5] = board[i+1][j+2];
                tmp[6] = board[i+2][j];
                tmp[7] = board[i+2][j+1];
                tmp[8] = board[i+2][j+2];

                if (hasDuplicate(tmp)) {
                    return false;
                }
            }
        }

        return true;
    }
}
