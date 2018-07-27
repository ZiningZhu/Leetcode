
class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Generate all permutations; get the k^th one; TLE. Passed 52/200 cases.

        # Pattern matching
        factorials = [1]  # factorials[n] is n!
        c = 1
        while len(factorials) <= n:
            factorials.append(c)
            c *= len(factorials)

        k -= 1  # Switch to zero-based index
        candidates = list(range(1, n+1))
        res = []

        while len(candidates) > 0:
            m = factorials[len(candidates)-1]
            i = int(k // m)
            k = k % m
            c = candidates.pop(i)
            res.append(str(c))

        return "".join(res)
