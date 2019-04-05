class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        ri = -1  # Rightmost increasing 
        if len(nums) == 1:
            return
        while i < len(nums) - 1:
            if nums[i] < nums[i+1]:
                ri = i
            i += 1
        
        if ri == -1:  
            self.reverse(nums, 0, len(nums))
        else:
            j = ri + 1
            while j < len(nums) and nums[j] > nums[ri]:
                j += 1
            nums[ri], nums[j-1] = nums[j-1], nums[ri]
            self.reverse(nums, ri+1, len(nums))

    def reverse(self, nums, start, end):
        i = start
        j = end - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
       