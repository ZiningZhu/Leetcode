/*
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
*/

public class Solution {
    public int search(int[] nums, int target) {
        if (nums.length==0) return -1;

        // Binary search to find breakpoint, then binary search to find the target.
        int i=0, j = nums.length;
        int mid = (i+j) / 2;
        while (j - i > 1) {
            if (nums[mid] < nums[i]) {
                j = mid;
                mid = (i + j) / 2;
            } else {
                i = mid;
                mid = (i + j) / 2;
            }
        }
        int piv = mid;
        if (piv == nums.length-1) {
            piv = -1;
        }
        //System.out.println("piv=" + piv);
        if (piv == -1) {
            int x=0, y=nums.length;
            while (y-x > 1) {
                mid = (x+y) / 2;
                if (nums[mid] == target) return mid;
                if (nums[mid] < target) {
                    x = mid;
                    mid = (x+y)/2;
                } else {
                    y = mid;
                    mid = (x+y)/2;
                }
            }
            return nums[mid] == target? mid : -1;
        } else {
            int x = 1, y=nums.length+1; // (Their indices + piv) % nums.length is the real index
            while ((y-x) > 1) {
                mid = (x + y) / 2;
                if (nums[(mid+piv)%nums.length] == target) return (mid+piv)%nums.length;
                if (nums[(mid+piv)%nums.length] < target) {
                    x = mid;
                    mid = (x + y) / 2;
                } else {
                    y = mid;
                    mid = (x + y) / 2;
                }
            }
            return nums[(mid+piv)%nums.length] == target? ((mid+piv)%nums.length) : -1;

        }
    }
}
