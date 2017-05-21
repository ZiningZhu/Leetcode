class Solution(object):
    def fractionAddition(self, expression):
        from itertools import groupby
        from fractions import Fraction
        sign = 1
        fra = [0, 0]
        part = 0
        ans = Fraction(0, 1)
        for k, v in groupby(expression, lambda x: x.isdigit()):
            w = "".join(v)
            if not k:
                if w == '+':
                    sign = 1
                elif w == '-':
                    sign = -1
                elif w == '/':
                    pass
            else:
                fra[part] = int(w)
                part ^= 1
                if part == 0:
                    ans += Fraction(sign*fra[0], fra[1])
        return "{}/{}".format(ans.numerator, ans.denominator)


''' Notes:
1. itertools.groupby(object, keyfunc)
- Seperate a new group whenever the key function evaluation (recorded in k) changes
- The grouped content is stored in v
2. fractions.Fraction avoids manually calculating gcd.
3. Basic idea is just convert the input string into tokens, read them in sequence, and process
'''
