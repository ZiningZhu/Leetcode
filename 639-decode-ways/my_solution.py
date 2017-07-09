class Solution:
    def cnt(self, s):
        if len(s) == 1:
            if (s == "*"):
                return 9
            elif (s == "0"):
                return 0
            else:
                return 1
        elif len(s) == 2:
            if (s[0] == "0"):
                return 0
            if (s[0] == "1"):
                if (s[1] == "*"):
                    return 9
                else:
                    return 1
            if (s[0] == "*"):
                if (s[1] == "*"):
                    return 15 # Careful here. * can only represent 1-9, not 0
                else:
                    if (int(s[1]) <= 6):
                        return 2
                    else:
                        return 1

            if (s[0] == "2"):
                if s[1] == "*":
                    return 6
                else:
                    if (int(s[1]) > 6):
                        return 0
                    else:
                        return 1
            else:
                return 0
        else:
            return 0

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # N[i] - number of ways to decode s[:i]
        # N[i+1] = N[i] * cnt(s[i]) + N[i-1] * cnt(s[i-1:i+1])
        # Base case - N[1], N[2]

        if (len(s) == 0):
            return 0
        elif len(s) == 1:
            return self.cnt(s[0])

        N = [0] * (len(s) + 1)
        N[0] = 1
        N[1] = self.cnt(s[0])


        for i in range(1, len(s)):
            N[i+1] = (N[i] * self.cnt(s[i]) + N[i-1] * self.cnt(s[i-1:i+1])) % (10**9 + 7)


        return N[len(s)]
