class Solution(object):
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # Remember an important theorem from Abstract Algebra:
        # any cycle group can be decomposed into products of transpositions (two-element cycle)
        # So the K>=2 operations (which are equivalent to a transposition, plus a shift),
        # can permute all possible sequences.
        if K >= 2:
            return "".join(sorted(list(S)))

        # The case is easy for K=1
        s2 = S + S
        minstr = unicode(chr(ord('z')+1) * len(S))  # unicode() is Python 2 only
        for i in range(len(S)):
            s = s2[i:i+len(S)]
            if unicode(s) < minstr:
                minstr = unicode(s)
        return str(minstr)
