class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        A = [0] * (len(nums))
        # A[i] contains the most money acquired from home 0, ..., i while taking nums[i]
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)

        A[0] = nums[0]
        A[1] = nums[1]
        for i in range(2, len(A)):
            A[i] = A[i-2] + nums[i]
            if i > 2:
                A[i] = max(A[i], A[i-3] + nums[i])
        return max(A[-1], A[-2])
