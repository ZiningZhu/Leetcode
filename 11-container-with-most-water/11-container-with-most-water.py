class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        '''
        # Brute force: for each two lines, decide its water holding capacity. O(n^2) time.
        # Time limit exceeded
        maxwater = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                curwater = (j-i) * min(height[i], height[j])
                if (curwater > maxwater):
                    maxwater = curwater
        return maxwater
        '''
        # Alternative method: two pointer. O(n) time.
        # Why does it work? https://discuss.leetcode.com/topic/503/anyone-who-has-a-o-n-algorithm/2
        maxwater = 0
        i = 0
        j = len(height) - 1
        while (i != j):

            curwater = (j - i) * min(height[i], height[j])
            if (curwater > maxwater):
                maxwater = curwater
            if (height[i] < height[j]):
                i += 1

            else:
                j -= 1
                
        return maxwater



if __name__ == "__main__":
    s = Solution()
    print "Should be 0: %d" %s.maxArea([1])
    print "Should be 6: %d" %s.maxArea([3, 1, 4])
    print "Should be 4: %d" %s.maxArea([1, 2, 4, 3])
    print "Should be 9: %d" %s.maxArea([2, 4, 1, 5, 3])
