class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        fd = {}
        for c in s:
            if c in fd:
                fd[c] += 1
            else:
                fd[c] = 1
        keys = fd.keys()
        keys.sort(key=lambda k: -fd[k])
        ret = []
        for k in keys:
            for i in range(fd[k]):
                ret.append(k)
        return "".join(ret)
