class Solution:
    def numTrees(self, n: int) -> int:
        self.memDict = {}
        return self.bstFinder(1, n+1)

    def bstFinder(self, start: int, end: int):
        q = end - start
        if q in self.memDict:
            return self.memDict[q]

        if q <= 0:
            return 1

        a = 0
        for i in range(start, end):
            a += self.bstFinder(start, i) * self.bstFinder(i+1, end)
        self.memDict[q] = a
        return a
