class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        # Modified DFS to check bi-partite-able
        M = [[] for i in range(N+1)]
        for d in dislikes:
            M[d[0]].append(d[1])
            M[d[1]].append(d[0])

        colors = [0] * (N+1)
        for i in range(1, N+1):
            if colors[i] == 0:  # unvisited at all
                colors[i] = 1
                if not self.bi_partite_able(i, M, colors):
                    return False
        return True

    def bi_partite_able(self, u, M, colors):
        ok = True
        for v in M[u]:
            if colors[v] == 0:
                colors[v] = -colors[u]  # assign to opposite queue
                if not self.bi_partite_able(v, M, colors):
                    return False
            else:
                if colors[v] != -colors[u]:
                    # someone assigned it to a different queue (in this tree -- since v is connected to u)
                    return False
                # Also you don't need to DFS from here again, since v is visited before.
        return True




        
