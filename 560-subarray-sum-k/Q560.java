public class Solution {
    public int subarraySum(int[] nums, int k) {
        int n = nums.length;
        if (n==0) {
            return 0;
        }
        //int[][] sums = new int[n][n];
        int cursum = 0;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            cursum = nums[i];
            //sums[i][i] = cursum;
            if (cursum == k)
                ans += 1;
            for (int j = i+1; j < n; j++) {
                cursum = cursum + nums[j];
                if (cursum == k) {
                    ans += 1;
                }
            }

        }
        return ans;
    }
}
