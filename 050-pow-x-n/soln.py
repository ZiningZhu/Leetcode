# Implement pow(x, n), which calculates x raised to the power n (x ** n).
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [-2**31, 2**31-1]

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # Notice that n is large.
        # x^{sum of n_i} = mult of {x^n_i}
        # where x^{n_i} can be calculated easily when n_i is 2**i
        ret = 1.0
        mult = x
        i = 0
        n_rem = abs(n)
        while i <= 31 and n_rem > 0:  # Careful about max i: it can be 31

            if n_rem & 1:  # The last bit of n is 1
                ret *= mult
            mult *= mult  # mult is x**(2**i)
            n_rem = n_rem >> 1
            i += 1

        if n >= 0:
            return ret
        else:
            print "n < 0"
            return 1 / ret
