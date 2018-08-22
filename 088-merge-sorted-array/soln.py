class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                for k in range(m, i, -1):
                    nums1[k] = nums1[k-1]
                nums1[i] = nums2[j]
                m += 1
                j += 1

        while j < n:
            nums1[i] = nums2[j]
            i += 1
            j += 1
        
