# Problem: https://leetcode.com/problems/trapping-rain-water/description/
# It should be the only question I can remember when interviewing at Needham


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        top = [0] * len(height)
        max_from_left = [0] * len(height)
        max_from_right = [0] * len(height)

        max_left = 0
        max_right = 0
        for i in range(len(height)):
            if height[i] > max_left:
                max_left = height[i]
            max_from_left[i] = max_left
            if height[len(height)-i-1] > max_right:
                max_right = height[len(height)-i-1]
            max_from_right[len(height)-i-1] = max_right
        for i in range(len(height)):
            top[i] = min(max_from_left[i], max_from_right[i])


        total = 0
        for i in range(len(height)):
            total += (top[i] - height[i])
        return total
