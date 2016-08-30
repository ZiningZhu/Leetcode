class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        possible input situations:
        (1) Whitespaces at the front
        (2) Take the first non-whitespace character. Plus or minus
        (3) Size limitation and error handling (return 0 if non convertible)
        """
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        starting_whitespace = True
        sign_recorded = False
        sign = 1
        res = 0
        for i in range(len(str)):
            if starting_whitespace:
                if (str[i] == " "):
                    continue
                else:
                    starting_whitespace = False

            if not sign_recorded:
                sign_recorded = True
                if (str[i] == "-"):
                    sign = -1
                    continue
                elif (str[i] == "+"):
                    sign = 1
                    continue
                else:
                    sign = 1


            if not str[i].isdigit():
                break
            else:
                res = res * 10 + int(str[i])
        res = min(INT_MAX, max(INT_MIN, sign * res))
        return res


if __name__ == "__main__":
    s = Solution()
    print "Should be 0: %d" %s.myAtoi("")
    print "Should be 1: %d" %s.myAtoi("1")
    print "Should be 1: %d" %s.myAtoi("+1")
    print "Should be -1: %d" %s.myAtoi(" -1")
    print "Should be -1: %d" %s.myAtoi("  -1px")
    print "Should be 0: %d" %s.myAtoi("- 1")
