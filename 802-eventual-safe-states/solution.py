# https://leetcode.com/articles/find-eventual-safe-states/

class Solution(object):
    """
    Recursive DFS solution: use three colors. Different from BFS, DFS is able to
    figure out if all nodes along this path are safe.
    """
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        WHITE, GRAY, BLACK = 1, 2, 3
        colors = [WHITE] * len(graph)

        def dfs(node):  # return False if this pt is unsafe
            if colors[node] == BLACK:
                return True
            if colors[node] == GRAY:
                return False

            colors[node] = GRAY
            for n in graph[node]:
                if colors[n] == BLACK:
                    continue
                if colors[n] == GRAY or dfs(n) == False:
                    return False

            colors[node] = BLACK
            return True

        return filter(dfs, range(len(graph)))

"""Alternative solution: reverse graph. Go from the safe ending points. If no
cycle is encountered, the path is safe. See @awice's explanation on the solution
"""
