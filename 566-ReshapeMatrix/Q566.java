public class Solution {
    public int[][] matrixReshape(int[][] nums, int r, int c) {
        int n = nums.length;
        int m;
        if (n>0) {
            m = nums[0].length;
        } else {
            return nums;
        }
        //System.out.println(String.format("n=%d. m=%d", n, m));
        if (n*m != r*c) {
            return nums;
        } else {
            int[][] result = new int[r][c];
            int ro=0, co=0, rt=0, ct=0;
            for (int i=0; i<(r*c); i++) {
                //System.out.println(String.format("i=%d, result[%d][%d]=nums[%d][%d]", i, rt, ct, ro, co));
                result[rt][ct] = nums[ro][co];
                co++; ct++;
                if (co == m) {
                    co = 0;
                    ro++;
                }
                if (ct == c) {
                    ct = 0;
                    rt++;
                }
            }
            return result;
        }

    }
}
