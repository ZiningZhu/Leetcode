class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        unvisited = {}
        visited = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    unvisited[(i, j)] = 0
                    visited[(i, j)] = 0
        num_islands = 0
        while len(unvisited) > 0:
            start = list(unvisited.keys())[0]

            queue = [start]
            num_islands += 1
            while len(queue) > 0:
                curr = queue.pop(0)

                i, j = curr
                visited[(i, j)] = 1
                if (i, j) in unvisited:
                    unvisited.pop((i, j))
                else:
                    continue
                if i-1 >= 0 and grid[i-1][j] == '1' and not visited[(i-1, j)]:
                    queue.append((i-1, j))
                if i+1 < len(grid) and grid[i+1][j] == '1' and not visited[(i+1, j)]:
                    queue.append((i+1, j))
                if j-1 >= 0 and grid[i][j-1] == '1' and not visited[(i, j-1)]:
                    queue.append((i, j-1))
                if j+1 < len(grid[0]) and grid[i][j+1] == '1' and not visited[(i, j+1)]:
                    queue.append((i, j+1))
        return num_islands

                    
