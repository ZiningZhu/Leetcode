class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if (x < 0):
            sign = -1
            x = -x
        counting_start_zeros = True
        num_zeros = 0
        res = 0
        while(x > 0):
            head = x % 10
            x = int(x // 10)
            if counting_start_zeros:
                num_zeros += 1
            if (head != 0):
                counting_start_zeros = False
            if not counting_start_zeros:
                res = res * 10 + head

        # Handling overflow; required by the question
        if ((sign == -1 and res > 2**32) or res >= 2**32 ):
            return 0
        return sign * res


if __name__ == "__main__":
    s = Solution()
    print "Should be 0: %d" %s.reverse(0)
    print "Should be -1: %d" %s.reverse(-1)
    print "Should be 321: %d" %s.reverse(123)
    print "Should be 1: %d" %s.reverse(1000)
