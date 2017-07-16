class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Because this question only asks for an approximate answer (and brute-force time-outs, and DP is not obvious yet)
        # Binary search to find whether an average is achievable is used

        lo = -10001
        hi = 10001
        mid = (lo + hi) / 2.0

        while (hi - lo > 0.00001):
            if (self.achievable(nums, mid, k)):
                lo = mid
                mid = (lo + hi) / 2.0
            else:
                hi = mid
                mid = (lo + hi) / 2.0
        return mid

    def achievable(self, nums, mid, k):
        sums = 0
        for i in range(k):
            sums += (nums[i] - mid)

        if sums >= 0:
            return True

        prev = 0
        min_prev = prev
        for i in range(k, len(nums)):
            sums += (nums[i] - mid)
            prev += (nums[i-k] - mid)
            if (prev < min_prev):
                min_prev = prev
            if (sums - min_prev >= 0):
                return True
        return False

# 185ms. TLE although same algorithm as Java LOL
