class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        used = {}
        for c in s:
            if c in used:
                used[c] += 1
            else:
                used[c] = 1
        for c in t:
            if c in used:
                used[c] -= 1
                if used[c] < 0:
                    return False
            else:
                return False
        for c in used:
            if used[c] != 0:
                return False
        return True
            
