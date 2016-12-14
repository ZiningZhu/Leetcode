class Solution(object):
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mymap = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        slist = digits.strip()
        cleanInt = []
        for i in range(len(slist)):
            if slist[i] in mymap:
                cleanInt.append(i)
        resList = []
        i = 0
        while(i < len(slist)):
            print "****i=%d****" %i
            newlist = []
            if len(resList) == 0:
                newlist = mymap[slist[i]]
            for j in range(len(resList)):
                
                for k in range(len(mymap[resList[i]])):
                    newlist.append(reslList[j] + mymap[slist[i]][k])
            resList[:] = newlist[:]
            i += 1
        return resList
            
            
if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))