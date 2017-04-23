# Accepted brute force solution

class Solution(object):
    def longest(self, v):
        ans = 0
        counter = 0
        if v[0] == 1:
            counter = 1
            if counter > ans:
                ans = counter
        for i in range(1, len(v)):
            if v[i] == 1:
                if v[i] == v[i-1]:
                    counter += 1
                else:
                    counter = 1
                if counter > ans:
                    ans = counter
            else:
                counter = 0
        #print ("v={},ans={}".format(v, ans))
        return ans




    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if len(M) == 0 or len(M[0]) == 0:
            #print ("Empty input!")
            return 0

        ans = 0
        for i in range(len(M)):
            t = self.longest(M[i])
            if t > ans:
                ans = t
        for j in range(len(M[0])):
            t = self.longest([M[i][j] for i in range(len(M))])
            if t > ans:
                ans = t

        Y = len(M)
        X = len(M[0])
        if Y > X:
            # '/'
            for k in range(X):
                i = k; j = 0; L=[]
                while i >= 0:
                    L.append(M[i][j])
                    i -= 1
                    j += 1
                t = self.longest(L)
                if t > ans:
                    ans = t
            for k in range(Y-X):
                i = X+k; j=0; L=[]
                while j < X:
                    L.append(M[i][j])
                    i -= 1
                    j += 1
                t = self.longest(L)
                if t > ans:
                    ans = t
            for k in range(1, X):
                i = Y-1; j = k; L=[]
                while (j < X):
                    L.append(M[i][j])
                    i -= 1
                    j += 1
                t = self.longest(L)
                if t > ans:
                    ans = t
            # '\'
            for k in range(X):
                i = 0; j = X-k-1; L=[]
                while (j < X):
                    L.append(M[i][j])
                    i += 1
                    j += 1
                t = self.longest(L)
                if t > ans:
                    ans = t
            for k in range(1, Y-X):
                i = k; j = 0; L = []
                while (j < X):
                    #print ("i={}, j={}, len(M)={}, len(M[0])={}".format(i,j,len(M), len(M[0])))
                    L.append(M[i][j])
                    i += 1
                    j += 1

                t = self.longest(L)
                if t > ans:
                    ans = t
            for k in range(X):
                i = Y-k-1; j = 0; L = []
                while (i < Y):
                    L.append(M[i][j])
                    i += 1
                    j += 1
                t = self.longest(L)
                if t > ans:
                    ans = t

        else: # Y <= X
            # '/'
            for k in range(Y):
                i=k; j=0; L=[]
                while (i>=0):
                    L.append(M[i][j])
                    i -= 1
                    j += 1
                t = self.longest(L)
                if t > ans:
                    ans = t

            for k in range(1, X-Y):
                i = Y-1; j = k; L=[]
                while (i >= 0):
                    L.append(M[i][j])
                    i -= 1
                    j += 1
                t = self.longest(L)
                if t > ans:
                    ans = t

            for k in range(Y):
                i=Y-1; j=X-1-k; L=[]
                while (j < X):
                    L.append(M[i][j])
                    i -= 1
                    j += 1
                t = self.longest(L)
                if t > ans:
                    ans = t

            # '\'
            for k in range(Y):
                i=0; j=X-1-k; L=[]
                while (j < X):
                    L.append(M[i][j])
                    i += 1
                    j += 1
                t = self.longest(L)
                if t > ans:
                    ans = t

            for k in range(1, X-Y):
                i = 0; j = k; L = []
                while (i < Y):
                    L.append(M[i][j])
                    i += 1
                    j += 1
                t = self.longest(L)
                if t > ans:
                    ans = t

            for k in range(Y):
                i = k; j = 0; L = []
                while (i < Y):
                    L.append(M[i][j])
                    i += 1
                    j += 1
                t = self.longest(L)
                if t > ans:
                    ans = t

        return ans


# Note1: Here is cleverer brute force solution: We do not need to seperate the cases!
# Basically pad the rectangle as I did, but reducing function calls speeds things up.
public class Solution {
    public int longestLine(int[][] M) {
        if (M.length == 0)
            return 0;
        int ones = 0;
        //horizontal
        for (int i = 0; i < M.length; i++) {
            int count = 0;
            for (int j = 0; j < M[0].length; j++) {
                if (M[i][j] == 1) {
                    count++;
                    ones = Math.max(ones, count);
                } else
                    count = 0;
            }
        }
        //vertical
        for (int i = 0; i < M[0].length; i++) {
            int count = 0;
            for (int j = 0; j < M.length; j++) {
                if (M[j][i] == 1) {
                    count++;
                    ones = Math.max(ones, count);
                } else
                    count = 0;
            }
        }
        //upper diagonal
        for (int i = 0; i < M[0].length || i < M.length; i++) {
            int count = 0;
            for (int x = 0, y = i; x < M.length && y < M[0].length; x++, y++) {
                if (M[x][y] == 1) {
                    count++;
                    ones = Math.max(ones, count);
                } else
                    count = 0;
            }
        }
        //lower diagonal
        for (int i = 0; i < M[0].length || i < M.length; i++) {
            int count = 0;
            for (int x = i, y = 0; x < M.length && y < M[0].length; x++, y++) {
                if (M[x][y] == 1) {
                    count++;
                    ones = Math.max(ones, count);
                } else
                    count = 0;
            }
        }
        //upper anti-diagonal
        for (int i = 0; i < M[0].length || i < M.length; i++) {
            int count = 0;
            for (int x = 0, y = M[0].length - i - 1; x < M.length && y >= 0; x++, y--) {
                if (M[x][y] == 1) {
                    count++;
                    ones = Math.max(ones, count);
                } else
                    count = 0;
            }
        }
        //lower anti-diagonal
        for (int i = 0; i < M[0].length || i < M.length; i++) {
            int count = 0;
            for (int x = i, y = M[0].length - 1; x < M.length && y >= 0; x++, y--) {
                //System.out.println(x+" "+y);
                if (M[x][y] == 1) {
                    count++;
                    ones = Math.max(ones, count);
                } else
                    count = 0;
            }
        }
        return ones;

    }
}

# Note 2: A Dynamic Programming Solution only traverses the matrix once, and keep track of the horizontal, vertical, diagonal and anti-diagonal consecutive 1's up till now. O(nm) time, O(nm) space.

public class Solution {
    public int longestLine(int[][] M) {
        if (M.length == 0)
            return 0;
        int ones = 0;
        int[][][] dp = new int[M.length][M[0].length][4];
        for (int i = 0; i < M.length; i++) {
            for (int j = 0; j < M[0].length; j++) {
                if (M[i][j] == 1) {
                    dp[i][j][0] = j > 0 ? dp[i][j - 1][0] + 1 : 1;
                    dp[i][j][1] = i > 0 ? dp[i - 1][j][1] + 1 : 1;
                    dp[i][j][2] = (i > 0 && j > 0) ? dp[i - 1][j - 1][2] + 1 : 1;
                    dp[i][j][3] = (i > 0 && j < M[0].length - 1) ? dp[i - 1][j + 1][3]+1 : 1;
                    ones = Math.max(ones, Math.max(Math.max(dp[i][j][0], dp[i][j][1]), Math.max(dp[i][j][2], dp[i][j][3])));
                }
            }
        }
        return ones;
    }
}
