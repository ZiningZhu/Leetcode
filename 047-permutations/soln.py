# Solution using dictionary to avoid collision before results. Beats 99.58% Python
# Recursive framework: a "path" parameter can be included to distinguish each run
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.permute(res, nums, [])
        return res

    def permute(self, res, nums, path):
        if len(nums) == 0:
            res.append(path)
            return

        dic = {x: 1 for x in nums}
        for i in range(len(nums)):
            if dic[nums[i]] == 1:
                self.permute(res, nums[:i] + nums[i+1:], path + [nums[i]])
                dic[nums[i]] = 0
        return

# Solution using hashing of results. Beats 99.75% Python
# Iterative BFS framework
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        stack = {}
        for i in range(len(nums)):
            c = nums[i]
            if len(stack) == 0:
                L = tuple([c])
                stack[L] = True
            else:
                ns = {}
                while len(stack) > 0:
                    tL = stack.keys()[0]
                    L = list(tL)
                    del stack[tL]
                    for j in range(len(L)+1):
                        nL = L[:]
                        nL.insert(j, c)
                        tnL = tuple(nL)
                        if tnL not in ns:
                            ns[tnL] = True
                stack = ns
        return stack.keys()
