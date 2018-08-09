class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        left = 0
        right = len(nums)-1
        mid = -1
        linear_search = False
        while right - left > 1:
            mid = (right + left) / 2
            if nums[right] < nums[left] and nums[mid] <= nums[right]:
                right = mid
            elif nums[right] < nums[left] and nums[left] < nums[mid]:
                left = mid
            else:
                linear_search = True  # Perform linear search in this case. e.g: [2,2,0,2,2,2,2]
                break  # No pivot found!
        if linear_search:
            return target in nums

        if len(nums) == 1:
            return nums[0] == target
        elif len(nums) == 2:
            return nums[0] == target or nums[1] == target
        else:
            pivot = right if nums[right] < nums[left] else left  # The actual smallest element
        print "pivot=", pivot

        low = pivot
        high = (pivot - 1) % len(nums)
        steps = 0
        while nums[high] == nums[low] and steps < len(nums):
            high = (high - 1) % len(nums)
            steps += 1
        mid = pivot

        if nums[low] > target or nums[high] < target:
            return False
        if nums[low] == target or nums[high] == target:
            return True
        while (high + len(nums) - low) % len(nums) > 1:
            if high > low:
                mid = (high + low) / 2
            else:
                mid = ((high + len(nums) + low) / 2) % len(nums)
            print low, high, mid

            if nums[mid] < target:
                low = mid
            elif nums[mid] > target:
                high = mid
            else:
                return True
        return nums[low] == target or nums[high] == target
