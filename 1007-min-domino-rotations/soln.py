class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        min_flip = float("inf")

        for target in range(1, 7):

            cost_a = 0
            cost_b = 0
            for i in range(len(A)):
                if A[i] != target and B[i] != target:
                    cost_a = float("inf")
                    cost_b = float("inf")
                    break
                if A[i] == target and B[i] != target:
                    cost_b += 1
                if B[i] == target and A[i] != target:
                    cost_a += 1

            #print ("target={}, cost_a={}, cost_b={}".format(target, cost_a, cost_b))
            cost = min(cost_a, cost_b)
            min_flip = min(min_flip, cost)

        if min_flip == float("inf"):
            return -1
        else:
            return min_flip

                
