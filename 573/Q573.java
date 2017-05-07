public class Solution {

    private int mdist(int[] a, int[] b) {
        return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
    }
    public int minDistance(int height, int width, int[] tree, int[] squirrel, int[][] nuts) {
        // Construct a Manhattan distance map of each nut from the tree
        // and one from squirrel to all nuts.
        // Total distance = 2 * [Sum of Mdist(nut, tree)] - Mdist(tree, nut_0) + Mdist(squirrel, nut_0)
        // The choice of nut_0 minimizes the term (-Mdist(tree, nut_0) + Mdist(squirrel, nut_0))

        int N = tree.length;
        if(N==0) {
            return 0;
        }
        System.out.println("Test");
        int[] md_tr = new int[N];
        int[] md_sq = new int[N];
        int[] diff = new int[N];
        int minterm = 9999999;
        int minidx = -1;
        for (int i=0; i < N; i++) {
            md_tr[i] = Math.abs(tree[0] - nuts[i][0]) + Math.abs(tree[1] - nuts[i][1]);
            md_sq[i] = Math.abs(squirrel[0] - nuts[i][0]) + Math.abs(squirrel[1] - nuts[i][1]);
            diff[i] = md_sq[i] - md_tr[i];
            if (diff[i] < minterm) {
                minterm = diff[i];
                minidx = i;
            }
        }
        int res = 0;
        for (int i = 0; i < N; i++) {
            res += (2 * md_tr[i]);
        }
        res += minterm;
        return res;
    }
}
