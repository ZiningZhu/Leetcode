# https://leetcode.com/articles/minimum-swaps-to-make-sequences-increasing/

class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n1 = 0  # The max swap used to make A[:i-1] (not including i-1) in order without swapping A[i-1]
        s1 = 1  # ... with swapping A[i-1]
        for i in range(1, len(A)):
            n2 = s2 = float("inf")

            if A[i] > A[i-1] and B[i] > B[i-1]:
                # Column i-1 and i are both natural or both swapped
                n2 = min(n2, n1)
                s2 = min(s2, s1 + 1)

            if A[i] > B[i-1] and B[i] > A[i-1]:
                # Column i-1 and i are {swapped, natural} or {natural, swapped}
                n2 = min(s1, n2)
                s2 = min(n1+1, s2)

            n1 = n2
            s1 = s2
        return min(n1, s1)
