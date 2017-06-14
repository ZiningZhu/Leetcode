/*
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
*/

public class Solution {
    public int[] searchRange(int[] nums, int target) {
        int lo=0, hi=nums.length-1;
        int mid=-1;
        if (nums.length==0) {
            return new int[] {-1,-1};
        }
        while (lo < hi) {
            mid = (lo + hi) / 2;
            if (nums[mid] == target) break;
            if (nums[mid] < target) {
                lo = mid+1;
            } else {
                hi = mid-1;
            }
        }
        mid = (lo + hi) / 2;
        if (nums.length==1 && nums[0]==target) {
            return new int[] {0, 0};
        }
        if (mid==-1 || nums[mid] != target) {
            return new int[] {-1, -1};
        }
        // Now mid is equal to target
        int st = mid, en = mid;
        //System.out.println("mid=" + mid);
        while (st>=0 && nums[st]==nums[mid]) st--;
        while (en<nums.length && nums[en]==nums[mid]) en++;
        int[] ans = new int[] {st+1, en-1};
        return ans;
    }
}
