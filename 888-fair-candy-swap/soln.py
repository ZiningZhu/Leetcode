class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = sum(B) - sum(A)
        # Just find two elements that differ by diff. O(n^2) gives TLE
        """
        for i in range(len(A)):
            for j in range(len(B)):
                if 2 * (B[j] - A[i]) == diff:
                    return [A[i], B[j]]
        """
        # Cache. AC
        dic_a = {}
        for i in range(len(A)):
            if A[i] not in dic_a:
                dic_a[A[i]] = True
        for j in range(len(B)):
            expected_a = B[j] - (diff / 2)
            if expected_a in dic_a:
                return [expected_a, B[j]]
        
