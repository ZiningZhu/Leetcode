class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ret = []
        for w in words:
            word_match = True
            perm = {}
            for i in range(len(w)):
                if w[i] in perm:
                    if perm[w[i]] != pattern[i]:
                        word_match = False
                        break
                    else:
                        continue
                else:
                    perm[w[i]] = pattern[i]

            # Check plausibility of permutation
            if len(perm) != len(set(perm.values())):
                word_match = False

            if word_match:
                ret.append(w)
        return ret
