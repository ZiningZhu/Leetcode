public class Solution {
    public int removeDuplicates(int[] nums) {
        int ol = nums.length;
        int p1 = 0;
        int p2 = 0;
        while (p2 < nums.length) {
            while (p2 < nums.length-1 && nums[p2] == nums[p2+1]) {
                p2 = p2 + 1;
                ol--;
            }
            nums[p1] = nums[p2];
            p1++;
            p2++;
        }
        return ol;
    }
}
