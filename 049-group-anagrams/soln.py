class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        adict = {}
        for s in strs:
            key = "".join(sorted(s))  # This is how to solve anagram problem
            if key not in adict:
                adict[key] = [s]
            else:
                adict[key].append(s)
        ret = []
        for key in adict:
            ret.append(adict[key])
        return ret
