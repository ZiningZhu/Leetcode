class Solution(object):

    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ad = [0] * 121
        for a in ages:
            ad[a] += 1
        ret = 0
        for a in range(0, len(ad)):
            for b in range(a//2+7+1, a+1):
                if b != a:
                    ret += (ad[b] * ad[a])
                else:
                    ret += ad[a] * (ad[a] - 1)
        return ret
