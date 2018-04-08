class Solution(object):

    def _search(self, A, i, K, mem):
        """The solution of A[:i] partitioned into K neighboring subsets"""
        if K == 1:
            ret = 1.0 * sum(A[:i]) / i
            mem[i][K] = ret
            return ret
        elif mem[i][K] > 0:
            return mem[i][K]
        else:
            curbest = 0
            for j in range(K-1, i):
                curbest = max(curbest, self._search(A, j, K-1, mem) + 1.0 * sum(A[j:i]) / (i-j))
            mem[i][K] = curbest
            return curbest

    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        mem = [[0 for j in range(K+1)] for i in range(len(A) + 1)]

        return self._search(A, len(A), K, mem)
