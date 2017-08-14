class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Basic idea is to imitate the allocation. There are breakpoints (diff>1) that separates bags.
        # For each bag (represented by counts), check if it is possible by just splitting them
        # Note that consecutive integers does NOT include duplicates!
        counter = collections.Counter(nums)
        prev = None
        bag = []
        for x in sorted(counter):
            if (prev is None or x - prev == 1):
                bag.append(counter[x])
            else:
                if (not self.check(bag)):
                    return False
                bag = []
            prev = x

        if bag and not self.check(bag):
            return False

        return True

    def check(self, bag):
        # Simulate -- start and end depicts the starting and ending indices of objects
        start = []
        end = []
        prev = 0
        for i, c in enumerate(bag):
            if (c > prev):
                start += ([i]*(c-prev))
            elif (c < prev):
                end += ([i-1] * (prev-c))
            prev = c
        end += ([i] * prev)
        ans = (len(start) == len(end)) and all(e-s>=2 for s,e in zip(start, end))
        #print ("bag={}, start={}, end={}, ans={}".format(bag, start, end, ans))
        return ans
