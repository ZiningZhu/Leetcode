import java.util.*;

public class ThreeSum {
    public List<List<Integer>> threeSum(int[] nums) {
        if (nums.length < 3) {
            return new LinkedList<>();
        }
        Arrays.sort(nums);
        List<List<Integer>> res = new LinkedList<> ();
        // Convert the 3-sum into a 2-sum problem
        for (int p = 0; p < nums.length - 2; p++) {
            int lo = p+1;
            int hi = nums.length-1;
            int sum = 0 - nums[p];
            while (lo < hi) {
                if (nums[lo] + nums[hi] == sum) {
                    //System.out.println("Added [" + p + ", " + lo + ", " + hi + "]");
                    res.add(Arrays.asList(nums[p], nums[lo], nums[hi]));
                    while (lo < hi && nums[lo] == nums[lo+1]) lo++;
                    while (hi > lo && nums[hi] == nums[hi-1]) hi--;
                    lo++; hi--;
                }
                else if (nums[lo] + nums[hi] < sum) {
                    lo++;
                } else {
                    hi--;
                }
            }
            while (p+1 < nums.length && nums[p] == nums[p+1]) p++;
        }
        return res;
    }


    public static void main(String[] args) {
        ThreeSum t = new ThreeSum();
        int[] nums;
        nums = new int[] {};
        System.out.println("Should be []:" + t.threeSum(nums));
        nums = new int[] {1,2,3};
        System.out.println("Should be []:" + t.threeSum(nums));
        nums = new int[] {1,0,-1};
        System.out.println("Should be [[-1,0,1]]:" + t.threeSum(nums));
        nums = new int[] {-3, 1, 2};
        System.out.println("Should be [[-3, 1, 2]]:" + t.threeSum(nums));
        nums = new int[] {-1,0,1,2,-1,-4};
        System.out.println("Should be [[-1,-1,2],[-1,0,1]]:" + t.threeSum(nums));
        nums = new int[] {0, 0, 0};
        System.out.println("Should be [[0, 0, 0]]:" + t.threeSum(nums));


    }
}
