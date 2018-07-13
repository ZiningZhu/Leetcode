class Solution(object):
    """
    # This solution times out on long sets. Passed 1607/1808 test cases
    def isMatch(self, s, p):
        if len(s) == 0:
            if len(p) == 0:
                return True
            return p == "*"*len(p)

        if len(p) == 0:
            return False

        if s[0] == p[0] or p[0] == "?":
            return self.isMatch(s[1:], p[1:])

        if p[0] == "*":
            for i in range(0, len(s)+1):
                if self.isMatch(s[i:], p[1:]):
                    return True
            return False
        return False
    """
    def isMatch(self, s,p):
        i,j,s_star,p_star = 0,0,0,-1
        while i<len(s):
            if j<len(p) and (s[i]==p[j] or p[j]=='?'):
                i,j = i+1,j+1
            elif j<len(p) and p[j]=='*':
                s_star,p_star = i,j  # Provides an anchor to back track
                j+=1
            # Goes back to saved state (if there is one)
            elif p_star!=-1:
                s_star +=1
                i,j = s_star,p_star+1
            else:  # No saved state. Already at the end of stack.
                return False
        # Why can you discard the previous saved states?
        # Because when the second "*" is encountered, if there is a mismatch in all possibilities of left tree,
        # there is no possibility of success in the right trees.
        # Example: p = "*abc*". Since "abc" does not find a match, all states should be pruned.

        while j<len(p) and p[j]=='*':
            j+=1
        return j==len(p)
