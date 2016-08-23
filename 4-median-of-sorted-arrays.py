class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        '''
        i and j are pointers so that left side has A[0:i] and B[0:j], and right side has A[i:] and B[j:].
        Set up constraint i+j=(m+n+1)//2
        Binary search wrt i in A. To increase speed and avoid overflow, let A be the shorter list.
        '''
        if (len(nums1) > len(nums2)):
            A = nums2; B = nums1
            m = len(A); n = len(B)
        else:
            A = nums1; B = nums2
            m = len(A); n = len(B)

        i = 0
        j = (m + n + 1) // 2 - i
        lmax = -1
        rmin = -1
        imin = 0; imax = m;
        while(imin <= imax):
            # I switched to imin, imax representation instead of the step,
            # since the "step" constraint has tricky boundary (terminal) case...

            if (j > 0 and i < m and B[j-1] > A[i]):
                imin = i + 1
                i = (imin + imax) // 2
                j = (m + n + 1) // 2 - i


            elif (i > 0 and j < n and A[i-1] > B[j]):
                imax = i - 1
                i = (imin + imax) // 2
                j = (m + n + 1) // 2 - i


            else:

                if i==0:
                    lmax = B[j-1]
                elif j==0:
                    lmax = A[i-1]
                else:
                    lmax = max(A[i-1], B[j-1])
                if ((m + n) % 2 == 1):

                    return lmax
                if i==m:
                    rmin = B[j]
                elif j==n:
                    rmin = A[i]
                else:
                    rmin = min(A[i], B[j])
                return (lmax + rmin) / 2.0



if __name__ == "__main__":
    s = Solution()
    print "Should be 2: %f" %s.findMedianSortedArrays([1, 3], [2])
    print "Should be 2.5: %f" %s.findMedianSortedArrays([1, 2, 3], [4])
    print "Should be 3: %f" %s.findMedianSortedArrays([1, 2, 3], [4, 5])
    print "Should be 3.5: %f" %s.findMedianSortedArrays([1, 4, 5], [2, 3, 6])
