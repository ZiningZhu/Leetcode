class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False

        i = 0; tmp = x
        while(tmp > 0):
            tmp /= 10
            i += 1
        length = i
        i = 0; j = length-1
        while (i < j):
            if self.getDigit(x, i) != self.getDigit(x, j):
                return False
            i += 1
            j -= 1
        return True

    def getDigit(self, x, index):
        #print "index=%d" %index
        for i in range(index):
            x /= 10
            #print "i=%d" %i
        return x % 10

if __name__ == "__main__":
    s = Solution()

    print "Should be True: %s" %str(s.isPalindrome(0))
    print "Should be True: %s" %str(s.isPalindrome(11))
    print "Should be True: %s" %str(s.isPalindrome(10201))
    print "Should be False: %s" %str(s.isPalindrome(10))
    print "Should be False: %s" %str(s.isPalindrome(1200))
    print "Should be False: %s" %str(s.isPalindrome(-10101))
    print "Should be False: %s" %str(s.isPalindrome(-2147483648))
