public class Solution {
    public int findUnsortedSubarray(int[] nums) {
        /*
        int i=0;
        int j = nums.length-1;
        if (nums.length==0) {
            return 0;
        }
        int iprev = i;
        int jpost = j;
        while (i<nums.length && nums[iprev] <= nums[i]) {
            iprev = i;
            i += 1;
        }
        while (j>=0 && nums[jpost] >= nums[j]) {
            jpost = j;
            j -= 1;
        }
        return j-i+1 +2;
        // Counter example: [9,1,2,3,4,8]
        */

        // Sort the array. Return the span of subarray not being equal.
        int[] nums_sorted = new int[nums.length];
        for (int k=0; k<nums.length; k++) {
            nums_sorted[k] = nums[k];
        }

        Arrays.sort(nums_sorted);
        int i=0, j=nums.length-1;
        for (i=0; i<nums.length && nums[i] == nums_sorted[i]; i++) ;
        for (j=nums.length-1; j>=0 && nums[j]==nums_sorted[j]; j--) ;
        return (j-i+1<0) ? 0 : (j-i+1);
    }
}
