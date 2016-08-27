import json

class Solution(object):

    '''
    # Time limit exceeded: brute force. Algs from the Python recursive solution http://stackoverflow.com/questions/127704/algorithm-to-return-all-combinations-of-k-elements-from-n
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        cnd = [] # candidates without duplicate

        # Brutal force
        res = []
        for length in range(1, len(candidates)+1):
            combs = self.find_combination(candidates, length)
            #print "length=%d, combs=%s" %(length, str(combs))
            for c in combs:
                if (sum(c) == target and c not in res):
                    res.append(c)

        return res

    def find_combination(self, candidates, length):
        res = []
        for i in range(len(candidates)):
            if (length == 1):
                res.append([candidates[i]])
            else:
                for nxt in self.find_combination(candidates[i+1:], length-1):
                    res.append ([candidates[i]] + nxt)
        return res
    '''

    # simple recursive solution inspired by previous one.
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()
        raw_res = self.find_comb(candidates, target)
        res = []
        for i in range(len(raw_res)):
            if raw_res[i] not in res:
                res.append(raw_res[i])
        return res

    def find_comb(self, candidates, target):
        if (target <= 0):
            return [[]];
        res = []
        for i in range(len(candidates)):
            if (target - candidates[i] < 0):
                break
            for comb in self.find_comb(candidates[i+1:], target - candidates[i]):
                res.append([candidates[i]] + comb)
        return res

    # One step further optimization: https://discuss.leetcode.com/topic/11852/my-84ms-python-recursive-solution

if __name__ == "__main__":

    s = Solution()
    print "should be [[1]]: %s" %json.dumps(s.combinationSum2([1], 1))
    print "should be [[1, 2]]: %s" %json.dumps(s.combinationSum2([1, 2], 3))
    print "should be [[1,2,5],[1,7],[1,1,6],[2,6]]: %s" %json.dumps(s.combinationSum2([10,1,2,7,6,1,5], 8))
