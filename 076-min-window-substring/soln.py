class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Idea 1: DP idea taking O(n*w)
        # Use n*w vectors to represent what the windows contain.
        # But the w could be as large as n, which becomes n^2

        # Idea 2: Greedy
        # maintain two sentinels and a dictionary. Decide matching in O(1) time.
        # Expand right the window until you have a match;
        # Contract from left until you don't have a match.
        # Why does this guarantees finding the shortest match? Because:
        # (1) The shortest match will be included, and
        # (2) Once included, the contraction will eliminate all redundant elements.

        if len(s) == 0 or len(t) == 0:
            return ""
        minlen = len(s)
        minleft, minright = -1, -1

        need = {}
        for c in t:
            if c in need:
                need[c] += 1
            else:
                need[c] = 1

        left = 0
        unmatched = len(need)
        for right in range(len(s)):
            #print c, need, left, right, unmatched
            c = s[right]

            if c in need:
                need[c] -= 1
                if need[c] == 0:
                    unmatched -= 1

            while unmatched == 0:
                c = s[left]
                if c in need:
                    need[c] += 1
                    if need[c] > 0:
                        unmatched += 1

                if right - left + 1 <= minlen:
                    minlen = right - left + 1
                    minleft, minright = left, right

                left += 1
        return s[minleft:minright+1]


            
