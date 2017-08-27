class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ret = []
        i = 1
        j = n
        while (i <= j):
            ret.append(i)
            if (i == j):
                break
            ret.append(j)
            i += 1
            j -= 1
        ret[k:] = sorted(ret[k:])
        if (ret[k-2] < n/2):
            ret[k:] = list(reversed(ret[k:]))

        return ret
