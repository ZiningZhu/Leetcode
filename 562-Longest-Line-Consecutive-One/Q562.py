import copy
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

    def get(self,i,j):
        # Time limit exceeded if we do the virtual padding here
        #print ("i={}, j={}".format(i,j))
        # We already assumed there was a padding done on M.
        M = self.M
        N1 = len(M)
        N2 = len(M[0])
        if N1 > N2: # padded diff columns to the right
            diff = N1-N2
            if j >= N2:
                return None
            else:
                return M[i][j]
        else: # padded diff rows to the bottom
            diff = N2-N1
            if i >= N1:
                return None
            else:
                return M[i][j]


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


        N1 = len(M)
        N2 = len(M[0])
        diff = 0 # later t shall not exceed len(Mat)-diff
        '''
        # Memory limit exceeded if we brutally do all the paddings
        if N1 > N2:
            diff = N1 - N2
            for i in range(N1):
                M[i] += [None] * diff
        else:

            diff = N2 - N1
            M += [[None] * N2] * diff
        '''


        #print ("After padding, M is:{}, N1={}, N2={}".format(M, N1, N2))

        self.M = M
        N = N1
        if N2 > N1: N = N2
        # Forward (/), upper triangle
        for k in range(N):
            L = []
            i = k; j = 0
            while (i >= 0):
                L.append(self.get(i,j))
                i -= 1
                j += 1
            t = self.longest(L)
            if t > ans:
                if t <= (N-diff):
                    ans = t
                else:
                    ans = (N-diff)

        # Forward (/), lower triangle
        for k in range(N):
            L = []
            i = N-1; j = N-k-1
            while (j < N):
                L.append(self.get(i,j))
                i -= 1
                j += 1
            #print ("/: len(L)={}".format(len(L)))
            t = self.longest(L)
            if t > ans:
                if t <= (N-diff):
                    ans = t
                else:
                    ans = N - diff

        # Backward (\), upper triangle
        for k in range(N):
            L = []
            i = 0; j = N-k-1
            while (j < N):
                L.append(self.get(i,j))
                i += 1
                j += 1
            t = self.longest(L)
            #print ("L={}, t={}".format(L, t))
            if t > ans:
                if t <= (N-diff):
                    ans = t
                else:
                    ans = (N-diff)

        # Backward (\), lower triangle
        for k in range(N):
            L = []
            i = N-k-1; j=0
            while (j <= k):
                L.append(self.get(i,j))
                i += 1
                j += 1
            #print ("\: len(L)={}".format(len(L)))
            t = self.longest(L)
            if t > ans:
                if t <= (N-diff):
                    ans = t
                else:
                    ans = (N-diff)
        return ans
            
