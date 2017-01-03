public class Solution {
    // Alg 1: O(n^3) time, constant space
    public List<List<Integer>> fourSum(int[] nums, int target) {
        ArrayList<List<Integer>> res = new ArrayList<List<Integer>>();
        if (nums == null || nums.length < 4)
            return res;
        Arrays.sort(nums);
        if (nums[0] * 4 > target || nums[nums.length-1] * 4 < target)
            return res;
        for (int i = 0; i < nums.length-3; i++) {
            if (3 * nums[i+1] + nums[i]> target || 3 * nums[nums.length-1] + nums[i] < target)
                continue;
            for (int j = i+1; j < nums.length-2; j++) {
                int l = j+1;
                int r = nums.length-1;
                int dsum = target - nums[i] - nums[j];
                if (l >= r) continue;
                if (2 * nums[l] > dsum || 2 * nums[r] < dsum) {
                    continue;
                }
                while (l < r) {
                    if (nums[l] + nums[r] < dsum) {
                        l++;
                    } else if (nums[l] + nums[r] > dsum) {
                        r--;
                    } else {
                        List<Integer> tmp = Arrays.asList(nums[i], nums[j], nums[l], nums[r]);
                        if (!res.contains(tmp))
                            res.add(tmp);

                        l++;
                        r--;
                    }
                }
            }
        }
        return res;
    }
}
