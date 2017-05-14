'''
583. Delete Operation for Two Strings My SubmissionsBack To Contest

Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.

'''

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ''' # Cannot just count. Sequence also matters.
        dic1 = {}

        for c in word1:
            if c not in dic1:
                dic1[c] = 1
            else:
                dic1[c] += 1
        for c in word2:
            if c not in dic1:
                dic1[c] = -1
            else:
                dic1[c] -= 1
        ans = 0
        for k in dic1.keys():
            if dic1[k] < 0:
                ans -= dic1[k]
            else:
                ans += dic1[k]
        return ans
        '''
        '''
        # Longest common substring. Incorrect
        # Semantic array: C[i,j] is LCCS of word1[?:i] and word2[:?j]
        # answer is in the max of C[i,j]
        # Computational array: see below

        N1 = len(word1)
        N2 = len(word2)
        if N1 <= N2:
            N = N1
        else:
            N = N2

        C = [[0]*(N2+1) for i in range(N1+1)]

        maxnum = 0
        for i in range(1, N1+1):
            for j in range(1, N2+1):
                if word1[i-1] == word2[j-1]:
                    C[i][j] = C[i-1][j-1]+1
                    if C[i][j] > maxnum:
                        maxnum = C[i][j]

        print(C)

        return N1-maxnum+N2-maxnum
        '''
        # Should use longest common subsequence. Not continuous.
        # Semantic array: C[i,j] is the LCS of A[1:i] and B[1:j]
        # Computational array: see below
        N1 = len(word1)
        N2 = len(word2)
        C = [[0] * (N2+1) for i in range(N1+1)]
        maxnum = 0
        for i in range(1, N1+1):
            for j in range(1, N2+1):
                if word1[i-1] == word2[j-1]:
                    C[i][j] = C[i-1][j-1] + 1
                    if C[i][j] > maxnum:
                        maxnum = C[i][j]
                else:
                    if C[i-1][j] > C[i][j-1]:
                        C[i][j] = C[i-1][j]
                    else:
                        C[i][j] = C[i][j-1]
        return N1 - maxnum + N2 - maxnum
