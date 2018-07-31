class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        # Very slow. Beat 4% Python
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix)):
                        if matrix[k][j] != 0:
                            matrix[k][j] = "0"
                    for k in range(len(matrix[0])):
                        if matrix[i][k] != 0:
                            matrix[i][k] = "0"
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    matrix[i][j] = 0
        """
        # Optimized: Beat 52% Python
        col0 = 1
        row0 = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0:
                        row0 = 0
                    if j == 0:
                        col0 = 0
                    else:
                        matrix[0][j] = 0 #if matrix[0][j] == 0 else "0"
                        matrix[i][0] = 0 #if matrix[i][0] == 0 else "0"
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        for i in range(len(matrix)):
            if col0 == 0:
                matrix[i][0] = 0
        for j in range(len(matrix[0])):
            if row0 == 0:
                matrix[0][j] = 0

                    
