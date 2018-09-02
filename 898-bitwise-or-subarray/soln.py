class Solution:
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # O(n^2) dynamic programming. TLE at a long test case
        """
        M = [[None for j in range(len(A)+1)] for i in range(len(A))]
        for i in range(len(A)):
            M[i][i+1] = A[i]
        for i in range(len(A)):
            for j in range(i+2, len(A)+1):
                M[i][j] = M[i][j-1] | A[j-1]
        D = {}
        for i in range(len(A)):
            for j in range(i+1, len(A)+1):
                if M[i][j] != None and M[i][j] not in D:
                    D[M[i][j]] = 1
        return len(D)
        """
        # Use set operations to optimize.
        # https://leetcode.com/problems/bitwise-ors-of-subarrays/discuss/165881/C++JavaPython-O(30N)
        # The complexity is still O(n^2), but "union" is faster than M[i][:], possibly because the duplicates are already eliminated.
        res = set()
        cur = set()
        for a in A:
            # cur stores all possible sequences ending at a.
            # cur is basically M[i][:], written in set.
            cur = {a} | {r|a for r in cur}
            res |= cur
        return len(res)
        
