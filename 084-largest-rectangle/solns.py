class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        """
        # DP: MemoryError at input [0,0,0,0,0,0,0,0,2147483647]
        if len(heights) == 0:
            return 0
        H = max(heights)
        M = [[0 for h in range(H+1)] for i in range(len(heights))]

        for h in range(1, 1+heights[0]):
            M[0][h] = h

        max_area = 0
        for i in range(1, len(heights)):
            for h in range(1, 1+heights[i]):
                M[i][h] = M[i-1][h] + h
                if M[i][h] > max_area:
                    max_area = M[i][h]
        return max_area
        """
        # Borrowing ideas from the rain drop container problem
        # https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28902/5ms-O(n)-Java-solution-explained-(beats-96)
        # A[i]: max rectangle with height heights[i]
        less_from_left = [-1 for i in range(len(heights))]
        less_from_right = [len(heights) for i in range(len(heights))]

        for i in range(1, len(heights)):
            j = i-1
            while j >= 0 and heights[j] >= heights[i]:  # This trick reduces time
                j = less_from_left[j]
            less_from_left[i] = j

        for i in range(len(heights)-2, -1, -1):
            j = i+1
            while j < len(heights) and heights[j] >= heights[i]:
                j = less_from_right[j]
            less_from_right[i] = j

        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area,
                          heights[i] * (less_from_right[i] - less_from_left[i] - 1))
        return max_area
