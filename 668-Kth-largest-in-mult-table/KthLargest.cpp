class Solution {
public:
    int findKthNumber(int m, int n, int k) {
        int low = 1, high = m * n;
        while (low != high) {
            int mid = (low + high) / 2;
            int cnt = 0;
            for (int i = 1; i <= m; ++i) {
                cnt += min(mid / i, n);
            }
            if (cnt < k) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return high;

    }
};

/*
This actually comes out from http://codeforces.com/contest/448/problem/D

What is the criteria for binary search? Compare cnt with k. Cnt should eventually be the number of mult table elements <= mid. Line 7-10 is a fast and clever way to do such counting.  
*/
