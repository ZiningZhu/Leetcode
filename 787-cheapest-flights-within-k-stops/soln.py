"""
When doing either DFS or BFS on graph, remember to check duplication in visiting!
In this problem, going to the same point is ok. Just need to avoid the A-B-A-B-...
infinite loop.
"""
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """

        num_cities = max([f[0] for f in flights] + [f[1] for f in flights]) + 1

        M = [[None for i in range(num_cities)] for j in range(num_cities)]
        for f in flights:
            M[f[0]][f[1]] = f[2]


        min_price = float("inf")
        q = [(src, -1, 0)]  # point, distance_covered, price
        min_prices = {}
        while len(q) > 0:
            _ = q.pop(0)
            #print _,
            curr_pt, curr_dist, curr_price = _[0], _[1], _[2]

            if curr_pt == dst:
                if curr_price < min_price:
                    min_price = curr_price

            if curr_price < min_prices.get(curr_pt, float("inf")):
                min_prices[curr_pt] = curr_price
                for n in range(len(M[curr_pt])):
                    if M[curr_pt][n] == None:
                        continue
                    edge_price = M[curr_pt][n]
                    if min_prices.get(n, False) and curr_price + edge_price >= min_prices[n]:
                        continue
                    nd = curr_dist + 1

                    if nd > K:
                        continue
                    np = curr_price + edge_price
                    q.append((n, nd, np))
            #print q

        return min_price if min_price < float("inf") else -1
