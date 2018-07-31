class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # Double-layer binary search. Beat 99.27%
        # Notices in binary search: (1) sentinels first set at 0 and len
        # and that never index at "end" sentinel (since it may be len)
        # (2) the stop criteria is end-start == 1
        # (3) After stopping, need an additional mid=(start+end)//2 step
        start = 0
        end = len(matrix)
        mid = 0
        while end - start > 1:
            mid = (start + end) // 2
            if matrix[mid][0] < target:
                start = mid
            elif matrix[mid][0] > target:
                end = mid
            else:
                return True

        # start is automatically the row where target is in (if exists)
        row = matrix[start]
        start = 0
        end = len(row)
        while end - start > 1:
            mid = (start + end) // 2
            if row[mid] < target:
                start = mid
            elif row[mid] > target:
                end = mid
            else:
                return True
        mid = (start + end) // 2
        return row[mid] == target

        
