class Solution(object):

    def find_comb(self, candidates, k, hist):
        if len(hist) == k:
            self.solutions.append(hist)
            return
        else:
            for i in range(len(candidates)):
                c = candidates[i]
                nh = hist[:]
                nh.append(c)
                nc = candidates[i+1:]  # Just discard candidates[:i]
                self.find_comb(nc, k, nh)

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        """
        # Soln 1: Beat 20%
        self.solutions = []
        self.find_comb(range(1, n+1), k, [])
        return self.solutions
        """

        # Soln 2: Beat 1%. Even slower. LOL
        # Combination: each element can be either in or out
        solutions = []
        combs = [[]]
        for i in range(1, 1+n):
            nc = []
            while len(combs) > 0:
                c = combs.pop()
                if len(c) == k:
                    solutions.append(c)
                else:
                    nc.append(c)
                    nc.append(c + [i])
            combs = nc
        solutions += filter(lambda c: len(c) == k, combs)
        return solutions

        
