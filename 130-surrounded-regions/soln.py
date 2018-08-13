class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # Intuitive solution that beats 5%. BFS all connected regions that does not contain boundary. Flip the region after BFS is done.
        dicts = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    dicts[(i,j)] = 0

        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        while len(dicts) > 0:
            start = dicts.keys()[0]
            boundary = False
            q = [start]
            region = []
            while len(q) > 0:
                curr = q.pop(0)
                region.append(curr)
                r, c = curr
                if curr in dicts:
                    dicts.pop(curr)
                else:
                    continue
                visited[r][c] = True

                if r == 0 or r == len(board)-1 or c == 0 or c == len(board[0])-1:
                    boundary = True

                if r > 0 and not visited[r-1][c] and board[r-1][c] == "O":
                    q.append((r-1, c))
                if r < len(board)-1 and not visited[r+1][c] and board[r+1][c] == "O":
                    q.append((r+1, c))
                if c > 0 and not visited[r][c-1] and board[r][c-1] == "O":
                    q.append((r, c-1))
                if c < len(board[0])-1 and not visited[r][c+1] and board[r][c+1] == "O":
                    q.append((r, c+1))
            #print region, boundary
            if not boundary:
                for curr in region:
                    r, c = curr
                    board[r][c] = "X"
