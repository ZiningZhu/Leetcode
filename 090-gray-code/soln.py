class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        else:
            L = self.grayCode(n-1)
            ret = L[:]
            head = 1 << (n-1)
            for i in range(len(L)-1, -1, -1):
                ret.append(L[i] + head)
            return ret
