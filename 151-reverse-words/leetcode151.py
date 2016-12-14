class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = s.strip(' ').split(' ')
        #print slist,
        #print len(slist)
        if (len(slist) == 0):
            return ""
        i = len(slist) - 1
        ans = ""
        while(i > 0):
            if (slist[i] == ''):
                i -= 1
                continue
            ans += (slist[i] + " ")
            i -= 1
        ans += slist[0].strip(" ")
        return ans
    
if __name__ == "__main__":
    s = Solution()
    #print (s.reverseWords(" "))
    print (s.reverseWords("    a    b"))
    #print (s.reverseWords(" Yo Brooo "))