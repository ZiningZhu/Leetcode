"""
A recap on bipartite graph checking: Color them by True or False. If such coloring
exists, this graph is bipartite.
Two details in this question:
(1) If there are multiple disjoing components in this graph, initialize a point
in each component (first_not_divisioned) to 0
(2) This is not going to cause conflict -- otherwise you are going to conflict
anyways
"""

class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        division = {}
        visited = {}
        tmp = self.first_not_divisioned(division, len(graph))
        while tmp >= 0:

            q = [tmp]
            #print tmp, q
            while len(q) > 0:
                #print "q", q,
                curr = q.pop(0)
                visited[curr] = True
                #print "curr", curr, "division", division
                if curr not in division:
                    division[curr] = 0
                for n in graph[curr]:
                    if n not in division:
                        division[n] = 1 - division[curr]
                    else:
                        if division[n] != (1 - division[curr]):
                            return False
                    if n not in visited:
                        q.append(n)

            tmp = self.first_not_divisioned(division, len(graph))
        return True

    def first_not_divisioned(self, division, N):
        for i in range(0, N):
            if i not in division:
                return i
        return -1
