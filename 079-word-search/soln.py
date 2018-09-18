class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        starts = []
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0]:
                    res = self.dfs(board, word, i, j, 0)
                    if res:
                        return True
        return False

    def dfs(self, board, word, i, j, k):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
            return False

        # Now visit (i, j)
        tmp = board[i][j]
        board[i][j] = "#"  # Avoid visiting again; don't use the "color" matrix

        if k == len(word)-1:
            return True

        has_result = self.dfs(board, word, i-1, j, k+1) or\
            self.dfs(board, word, i+1, j, k+1) or\
            self.dfs(board, word, i, j-1, k+1) or\
            self.dfs(board, word, i, j+1, k+1)

        board[i][j] = tmp
        return has_result
                
