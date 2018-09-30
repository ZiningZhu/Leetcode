class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        fd = {}
        for n in nums:
            if n in fd:
                fd[n] += 1
            else:
                fd[n] = 1
        keys = fd.keys()
        keys.sort(key=lambda k_: -fd[k_])
        return keys[:k]
