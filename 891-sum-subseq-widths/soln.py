class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        # There are 2**(len(A)) subsequences. Need to directly calculate.
        # n^2 solution still gets TLE.
        sums = 0
        max_val = 10**9 + 7

        # cache
        prods = [1]
        for i in range(len(A)):
            prods.append(prods[-1] * 2)

        # This is a crude optimization method: passed 43/64 cases but TLE
        """
        for j in range(len(A)-1, -1, -1):
            # There are 2**(j) subsequences with maxval A[j]
            prod = 1
            for i in range(j-1, -1, -1):
                sums = (sums + (A[j]-A[i]) * prod) % max_val
                prod *= 2
        """
        # This passed all 64 cases
        for j in range(len(A)):
            sums = (sums + (A[j] * prods[j])) % max_val
            sums = (sums - A[len(A)-j-1] * prods[j]) % max_val

        return sums
