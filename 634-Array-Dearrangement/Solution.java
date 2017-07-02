public class Solution {
    public int findDerangement(int n) {
        int N = (n>=4 ? n+1 : 4);
        long[] d = new long[N];
        d[0] = 0;
        d[1] = 0;
        d[2] = 1;
        d[3] = 2;
        for (int i=4; i<=n; i++) {
            d[i] = (i-1) * (d[i-1] + d[i-2]) % (1000000007);
        }
        return (int)d[n];
    }
}
/*A very good dynamic programming question. Just need you to think through the arrangement to realize d[n] = (n-1) * (d[n-1] + d[n-2]) */
