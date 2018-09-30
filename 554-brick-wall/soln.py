class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        # Figure out the boundaries. Compare them brute-force.
        boundaries = []
        for i in range(len(wall)):
            bd_row = []
            cur = 0
            for j in range(len(wall[i])-1):
                cur += wall[i][j]
                bd_row.append(cur)
            boundaries.append(bd_row)

        # Trick: if there are overlapping boundaries, then just take the most frequent one.
        fd = {}
        for bd_row in boundaries:
            for bd in bd_row:
                if bd not in fd:
                    fd[bd] = 1
                else:
                    fd[bd] += 1
        candidates = fd.keys()
        candidates.sort(key=lambda k: -fd[k])

        if len(candidates) == 0:
            return len(wall)

        best_loc = candidates[0]
        return len(wall) - fd[best_loc]
        
