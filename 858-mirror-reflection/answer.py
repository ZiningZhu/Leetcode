class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        height = 0
        i = 0
        while True:
            i = 1 - i
            height += q
            height %= (2 * p)
            if height == 0:
                return 0
            elif height == p:
                if i:
                    return 1
                else:
                    return 2
