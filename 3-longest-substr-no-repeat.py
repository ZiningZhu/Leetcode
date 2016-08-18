class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        noreplist = []
        ans = 0
        for i in range(len(s)):
            if s[i] in noreplist:
                n = noreplist.index(s[i])
                noreplist = noreplist[n+1:]
                noreplist.append(s[i])
            else:
                noreplist.append(s[i])
                if (len(noreplist) > ans):
                    ans = len(noreplist)
        return ans
