class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # This is combination problem.
        # Go by the definition of combination
        solutions = [[]]
        for i in range(len(nums)):
            ns = []
            while len(solutions) > 0:
                s = solutions.pop()
                ns.append(s)
                ns.append(s + [nums[i]])
            solutions = ns
        return solutions
