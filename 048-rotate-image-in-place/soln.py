# https://leetcode.com/problems/rotate-image/discuss/146406/5-Line-Python-Solution
#

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        assert len(matrix) == len(matrix[0])
        n = len(matrix)

        for i in range(int((n+1)/2)):  # This change makes it beat 100%
            for j in range(i, n-i-1):  # When x<y, range(x,y) gives []
                self.swap(matrix, i, j, n-j-1, i)
                self.swap(matrix, n-j-1, i, n-i-1, n-j-1)
                self.swap(matrix, n-i-1, n-j-1, j, n-i-1)

    def swap(self, matrix, x, y, i, j):
        tmp = matrix[x][y]
        matrix[x][y] = matrix[i][j]
        matrix[i][j] = tmp
