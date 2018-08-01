class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        a = 0  # nums[:a] are the "0" bucket
        b = len(nums)-1  # nums[b+1:] are the "2" bucket
        i = 0  # nums[:i] are processed.
        # Above are the loop invariants. When i finishes looping, nums is sorted.
        # Beat 100% pf Python solutions

        while i < len(nums):
            #print i, a, b, nums
            if i > b:
                break
            if nums[i] == 2:
                nums[i], nums[b] = nums[b], nums[i]
                i -= 1
                b -= 1
            elif nums[i] == 0 and i >= a:
                nums[i], nums[a] = nums[a], nums[i]
                i -= 1
                a += 1
            i += 1
