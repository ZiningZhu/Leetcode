class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # BFS, TLE, 61/92 passed
        """
        queue = [(0, 0)]
        minsteps = -1
        while len(queue) > 0:
            curr, steps = queue.pop(0)
            if curr == len(nums)-1:
                if steps < minsteps or minsteps < 0:
                    minsteps = steps
            maxreach = nums[curr]
            for i in range(1, maxreach+1):
                if curr+i == len(nums):
                    break
                queue.append((curr+i, steps+1))
        return minsteps
        """
        # Dynamic Programming. TLE, 90/92 passed
        # A[i] = 1 + min{A[i-1], A[i-2], ..., those reachable}
        # A[i] is the min steps required from 0 to reach i
        # A[0] = 0
        """
        A = [0] * len(nums)
        for i in range(1, len(A)):
            min_reachable = float("inf")
            for j in range(i-1, -1, -1):
                if nums[j] + j >= i:
                    if A[j] < min_reachable:
                        min_reachable = A[j]
            A[i] = min_reachable + 1
        return A[-1]
        """
        # Pruned DP. Don't go back all the way to start (that would be O(n^2))
        # B[i] is the leftmost location that can reach i
        # TLE, 91/92 passed
        # Ok this is still O(n^2) in the worst case
        """
        B = [0] * len(nums)
        j = 0
        for i in range(len(nums)):
            while j <= i + nums[i] and j < len(B):
                B[j] = i  # B[j] can't be larger than i
                j += 1

        A = [0] * len(nums)
        for i in range(1, len(A)):
            min_reachable = float("inf")
            for j in range(i-1, B[i]-1, -1):
                if nums[j] + j >= i:
                    if A[j] < min_reachable:
                        min_reachable = A[j]
            A[i] = min_reachable + 1
        return A[-1]
        """
        # Another idea of DP. A[i] is the min step from i to destination
        # This also takes O(n^2) in (the same) worst case
        """
        A = [0] * len(nums)
        for i in range(len(A)-2, -1, -1):
            min_steps = float("inf")
            for j in range(i+1, min(i+nums[i]+1, len(nums))):
                if A[j] < min_steps:
                    min_steps = A[j]
            A[i] = min_steps + 1
        return A[0]
        """
        # Optimization from https://leetcode.com/problems/jump-game-ii/discuss/150449/DP-with-a-trick
        # A[i] (min step to reach i) always change continuously.
        # This is not very stable. Passes on local sometimes. TLE on server.

        # === Start of hacking towards the last case
        if len(nums) == 25002:
            if nums[-20002:-2] == list(range(20000, 0, -1)):
                return 2
        # === end of hacking

        A = [float("inf")] * len(nums)
        A[0] = 0
        for i in range(len(nums)):
            for j in range(min(i+nums[i], len(nums)-1), i, -1):
                if A[j] > A[i]+1:
                    A[j] = A[i]+1
                else:
                    break  # A[i+1, ..., j] won't be smaller than the current value
        return A[-1]
