# Alg 1: Brute Force. O(n^3) time; Time Limit Exceeded
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlength = 0
        longest = ""
        for i in range(len(s)):
            for j in range(i+1, len(s) + 1):
                if (self.isPalindrome(s[i:j])):
                    if (j - i > maxlength):
                        maxlength = max(maxlength, j - i)
                        longest = s[i:j]
        return longest

    def isPalindrome(self, s):
        for i in range(len(s)):
            if (s[i] != s[len(s) - i - 1]):
                return False
        else:
            return True

# Alg 2: Dynamic Programming. O(n^2) time, O(n^2) space, Time limit exceeded. Note that (i, j) includes endpoint, while those in range() do not include the larger end point.
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ptable = {}
        start = 0; end = 1
        for i in range(len(s)):
            ptable[(i, i)] = True

        for curspan in range(2, len(s) + 1):
            for i in range(0, len(s) - curspan + 1):
                j = i + curspan - 1
                #print "i=%d, j=%d" %(i, j)

                if j==i+1 or ((i+1, j-1) in ptable and ptable[(i+1, j-1)]):
                    if (s[i] == s[j]):
                        ptable[(i, j)] = True
                        if (j - i + 1 > end - start):
                            start = i
                            end = j+1
                    else:
                        ptable[(i, j)] = False

        #print ptable
        return s[start:end]

# Alg 3: Dynamic Programming but with O(1) space. Expand from center
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0; end = 0
        for i in range(len(s)):
            (start1, end1, len1) = self.longestPalindromeExpand(s, i, i)
            (start2, end2, len2) = self.longestPalindromeExpand(s, i, i+1)
            if (len1 > end - start + 1):
                start, end = start1, end1
            if (len2 > end - start + 1):
                start, end = start2, end2

            #print "i=%d, (%d, %d), (%d, %d)" %(i, start1, end1, start2, end2)
        return s[start:end+1]

    def longestPalindromeExpand(self, s, i, j):
        start = i; end = j;

        while(start >= 0 and end < len(s)):
            if (s[start] == s[end]):
                start -= 1
                end += 1
            else:
                break
        start += 1
        end -= 1
        return (start, end, end-start+1)
