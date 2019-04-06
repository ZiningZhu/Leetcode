class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = [[]]
        nums = sorted(nums)
        k = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                k += 1
            else:
                k = 0
            nres = results[:]
            for p in results:
                if (i == 0 or nums[i] != nums[i-1]):
                    nres.append(p + [nums[i]])
                else:
                    # Only append if the final k elems of p are all nums[i]
                    if len(p) >= k and p[-k:] == [nums[i]] * k:
                        nres.append(p + [nums[i]])
            results = nres

        return results

        
