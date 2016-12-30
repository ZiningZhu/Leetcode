import java.util.*;


public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        // Stores <value -> pos mapping>. If the value key exists, there is an element corresponding

        for (int i = 0; i < nums.length; i++) {

            if (hm.get(target - nums[i]) != null) {
                int tmp = hm.get(target - nums[i]);
                if (i < tmp) {
                    int[] res = new int[] {i, tmp};
                    System.out.println(res.toString());
                    return res;
                } else {
                    int[] res = new int[] {tmp, i};
                    System.out.println(res.toString());
                    return res;
                }
            } else {
                System.out.println("putting "+nums[i] + " -> " + i);
                hm.put(nums[i], i);
            }
        }
        System.out.println("Answer not found!");
        return new int[] {-1, -1};

    }

    public static void main(String[] args) {
        int[] nums = new int[] {1, 2, 3, 4, 6};
        Solution sol = new Solution();
        System.out.println(sol.twoSum(nums, 6).toString());
    }
}
