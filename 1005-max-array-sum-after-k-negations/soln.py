class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:

        for i in range(K):
            minval = min(A)
            A[A.index(minval)] = -minval
        return sum(A)
