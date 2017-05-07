import java.util.*;

public class Solution {
    private int sfm;
    private int sfn;

    private boolean inRange(int x, int y) {
        if (x < 0 || x >= this.sfm || y < 0 || y >= this.sfn) {
            return false;
        } else {
            return true;
        }
    }
    public int findPaths(int m, int n, int N, int i, int j) {
        int MOD = 1000000007;
        if (N==0) {
            return 0;
        }
        this.sfm = m;
        this.sfn = n;
        int[][][] Mat = new int[N][m][n];
        int[] outs = new int[N];
        int x0 = i, y0 = j;
        for (i = 1; i < N; i++) {
            for (j = 1; j < m; j++) {
                Arrays.fill(Mat[i][j], 0);
            }
        }

        // Init step
        Mat[0][x0][y0] = 1;

        // Simulate
        for (i = 0; i < N; i++) {
            if (i>0) {
                for (int x = 0; x < m; x++) {
                    for (int y = 0; y < n; y++) {
                        int xt, yt;
                        xt = x-1;
                        yt = y;
                        if (this.inRange(xt, yt)) {
                            Mat[i][x][y] += Mat[i-1][xt][yt];
                            // int has range up to 2^31-1 = 2.147*10^7. No need to round here
                            Mat[i][x][y] %= MOD;
                        }
                        xt = x+1;
                        yt = y;
                        if (this.inRange(xt, yt)) {
                            Mat[i][x][y] += Mat[i-1][xt][yt];
                            Mat[i][x][y] %= MOD;
                        }
                        xt = x;
                        yt = y-1;
                        if (this.inRange(xt, yt)) {
                            Mat[i][x][y] += Mat[i-1][xt][yt];
                            Mat[i][x][y] %= MOD;
                        }
                        xt = x;
                        yt = y+1;
                        if (this.inRange(xt, yt)) {
                            Mat[i][x][y] += Mat[i-1][xt][yt];
                            Mat[i][x][y] %= MOD;
                        }
                    }
                }

            }

            // Take the answer: edge_only * 1 + corner_only * 2
            int ans = 0;
            for (int x = 0; x < m; x++) {
                ans = (ans + Mat[i][x][0]) % MOD;
                ans = (ans + Mat[i][x][n-1]) % MOD;
            }
            for (int y = 0; y < n; y++) {
                ans = (ans + Mat[i][0][y]) % MOD;
                ans = (ans + Mat[i][m-1][y]) % MOD;
            }
            outs[i] = ans;

        }

        /*
        // Debug: print out the simulation results
        for (i=0; i < N; i++) {
            System.out.println("Timestep " + i);
            for (j=0; j < m; j++) {
                System.out.println(Arrays.toString(Mat[i][j]));
            }
        }*/

        int finalans = 0;
        for (i=0; i<N; i++) {
            finalans = (finalans + outs[i]) % MOD;
        }
        return finalans;
    }
}
