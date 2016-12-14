class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        for i in range(len(t)):
            if t[i] not in d:
                return t[i]
            else:
                d[t[i]] -= 1
                if (d[t[i]] < 0):
                    return t[i]




if __name__ == "__main__":
    s = Solution()
    print "Should be 0: %s" %s.findTheDifference("", "0")
    print "Should be d: %s" %s.findTheDifference("abc", "adbc")
    print "Should be d: %s" %s.findTheDifference("abc", "cbad")
