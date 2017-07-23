class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key = lambda p : p[1])
        #print (pairs)

        length = 0
        curval = -2147483648
        for j in range(len(pairs)):
            pair = pairs[j]
            if (pair[0] > curval):
                length += 1
                curval = pair[1]
                continue

        return length
