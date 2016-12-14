class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        '''
        # brute force solution: O(n^2) time, O(1) space
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i, j]
        '''

        # hash table solution: O(n) time, O(n) space
        self.htable={} # a to a's index

        for n in range(len(nums)):
            if (target-nums[n]) in self.htable:
                ind = self.htable[target-nums[n]]
                return [min(n, ind), max(n, ind)]
            else:
                self.htable[nums[n]] = n
