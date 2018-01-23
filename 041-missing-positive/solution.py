"""Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while (nums[i] != i+1 and 0 < nums[i] <= len(nums)):
                #print "i=%d, nums=%s" % (i, str(nums))
                tmp = nums[nums[i]-1]  # Should use this swapping method -- python's a,b=b,a does not guarantee too clear atomic implementation
                nums[nums[i]-1] = nums[i]
                val = nums[i]  # [-10,-3,-100,-1000,-239,1]
                nums[i] = tmp
                if nums[i] == val:
                    nums[i] = -1

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1

"""
Solution idea: Place each item in its correct location (i.e: nums[i] = i+1).
For those out-out-range int, don't swap it -- leave it for be filled.
For those duplications, write in a garbage value.
"""
