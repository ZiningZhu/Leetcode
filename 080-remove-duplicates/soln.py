class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Brute iteration. Beat 1% solutions
        """
        length = 0
        for i in range(len(nums)):
            occurrence = 0
            for j in range(length):
                if nums[j] == nums[i]:
                    occurrence += 1
                if occurrence == 2:
                    break
            if occurrence < 2:
                nums[length] = nums[i]
                length += 1

        return length
        """
        # Ok the array is sorted. Beat 8% solutions.
        """
        length = 0
        for i in range(len(nums)):
            occurrence = 0
            for j in range(length-1, -1, -1):  # This goes back for at most 2 steps
                if nums[j] != nums[i]:
                    break
                occurrence += 1
            if occurrence < 2:
                nums[length] = nums[i]
                length += 1
        return length
        """
        # Can I be faster? Beat 31% solutions.
        """
        length = 0
        i = 0
        while i < len(nums)-1:
            while i < len(nums)-1 and nums[i] != nums[i+1]:
                nums[length] = nums[i]
                length += 1
                i += 1
            j = i+1
            duplicated = False
            while j < len(nums) and nums[j] == nums[i]:
                duplicated = True
                j += 1
            nums[length] = nums[i]
            length += 1
            if duplicated:
                nums[length] = nums[i+1]
                length += 1
            i = j
        if i == len(nums)-1:
            nums[length] = nums[i]
            length += 1
        return length
        """
        # Another solution: just include those not included more than twice. Beat 31% Python solutions
        # https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/27976/3-6-easy-lines-C++-Java-Python-Ruby
        length = 0
        for i in range(len(nums)):
            if i-2<0 or nums[i] > nums[length-2]:
                nums[length] = nums[i]
                length += 1
        return length
