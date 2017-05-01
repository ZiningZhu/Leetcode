class Solution(object):

    def allzeros(self, dicarr):
        #print ("Checking {}".format(dicarr))
        for i in dicarr:
            if i != 0:
                return False
        return True

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        # Sliding window solution
        dicarr = [0] * 26
        for c in s1:
            dicarr[ord(c) - ord('a')] += 1

        for i in range(len(s1)):
            c = s2[i]
            dicarr[ord(c) - ord('a')] -= 1
        if self.allzeros(dicarr):
            return True
        for i in range(len(s1), len(s2)):
            c = s2[i]
            prev = s2[i-len(s1)]
            dicarr[ord(c) - ord('a')] -= 1
            dicarr[ord(prev) - ord('a')] += 1
            #print "Window is s2(%d, %d]" %(i-len(s1), i)
            if self.allzeros(dicarr):
                return True
        return False
