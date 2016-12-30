class Solution(object):
    '''
    # Brute force: imitate human behavior. O(2n) time. Time limit exceeded.
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1):
            return s
        A = {}
        for i in range(numRows):
            A[i] = []

        for i in range(len(s)):
            k = i % (2*numRows-2)
            if (k < numRows):
                A[k].append(s[i])
            else:
                q = k - numRows + 1
                for j in range(numRows):
                    if (j + q == numRows - 1):
                        A[j].append(s[i])
                    else:
                        A[j].append(" ")

        #for i in range(numRows):
        #    print "%d: %s" %(i, str(A[i]))

        res = ""
        for i in range(numRows):
            for j in range(len(A[0])):
                if (j >= len(A[i])):
                    break
                if (A[i][j] != " "):
                    res += A[i][j]
        return res
    '''

    # Alg 2: directly assign the arrays. 148ms. O(n) time.
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if (numRows == 1):
            return s
        A = {}
        for i in range(numRows):
            A[i] = ""

        for i in range(0, len(s), 2*numRows-2):

            A[0] += s[i]
            for j in range(1, numRows-1):
                if (i+j >= len(s)):
                    continue
                elif (i + 2*numRows-2-j >= len(s)):
                    A[j] += s[i+j]
                else:
                    A[j] += (s[i+j] + s[i+(2*numRows-2-j)])
            if (i+numRows-1>=len(s)):
                continue
            else:
                A[numRows-1] += s[i+numRows-1]


        res = ""
        for i in range(numRows):
            #print A[i]
            res += A[i]
        return res

if __name__ == "__main__":
    s = Solution()
    print "Should be '': %s" %s.convert("", 1)
    print "Should be A: %s" %s.convert("A", 1)
    print "Should be AB: %s" %s.convert("AB", 2)
    print "Should be ACB: %s" %s.convert("ABC", 2)
    print "Should be ACBD: %s" %s.convert("ABCD", 2)
    print "Should be AEBDC: %s" %s.convert("ABCDE", 3)
    print "Should be AGBFHCED: %s" %s.convert("ABCDEFGH", 4)
