class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        A = [[0 for j in range(n+1)] for i in range(m+1)]
        # A[i][j] is the min edit distance from word1[:i] to word2[:j]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    A[0][j] = j
                elif j == 0:
                    A[i][0] = i
                elif word1[i-1] == word2[j-1]:
                    A[i][j] = A[i-1][j-1]
                else:
                    A[i][j] = 1 + min(A[i-1][j-1], A[i][j-1], A[i-1][j])
        return A[-1][-1]
