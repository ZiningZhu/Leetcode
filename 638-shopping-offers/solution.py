class Solution:
    def minPrice(self, cost, first_si, needs):
        # Base case: no more specials applied
        t = 0
        for i in range(len(needs)):
            t += self.price[i] * needs[i]
        if (cost + t < self.min_price):
            self.min_price = cost + t

        # Now attempt to apply any specials, if possible
        for si in range(first_si, len(self.special)):
            ok = True
            for i in range(len(self.price)):
                if (needs[i] < self.special[si][i]):
                    ok = False
                    break
            if ok:
                for i in range(len(self.price)):
                    needs[i] -= self.special[si][i]
                self.minPrice(cost + self.special[si][-1], si, needs)
                for i in range(len(self.price)):
                    needs[i] += self.special[si][i]


    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        # Just brutally search for the lowest possible of specials, using backtrack DFS search
        self.price = price
        self.special = special
        self.min_price = float("inf")
        self.minPrice(0, 0, needs)
        return self.min_price

# Each node dfs(needs, cost, last) evaluates a total price: cost + \sum_i price[i] * needs[i]
# Each node then expands by possible locations of the next applied coupon. 
