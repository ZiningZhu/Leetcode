class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        if len(candies) == 0:
            return 0

        candies.sort()
        cc = {}
        i=0
        cnt=0
        prev=None
        while i < len(candies):
            if candies[i] == prev:
                cnt += 1
                prev = candies[i]
            else:
                if prev == None:
                    prev = candies[i]
                    cnt = 1
                else:
                    cc[prev] = cnt
                    prev = candies[i]
                    cnt = 1


            i+= 1
        cc[prev] = cnt

        #print cc
        if len(cc) <= len(candies)/2:
            return len(cc)
        else:
            return len(candies)/2
