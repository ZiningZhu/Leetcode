class Solution:
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        hist = {}
        for i in range(N):
            nc = [0] * len(cells)
            for j in range(1, len(cells)-1):
                if (cells[j-1] + cells[j+1]) in [0, 2]:
                    nc[j] = 1
            cells = nc
            if i == N-1:
                return nc

            tnc = tuple(nc)
            if tnc not in hist:
                hist[tnc] = i
            else:

                n_res = (N-1) % i
                for ans in hist:
                    if hist[ans] == n_res:
                        return ans
        
