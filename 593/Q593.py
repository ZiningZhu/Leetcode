class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def D((a,b),(c,d)):
            return (c-a)**2 + (b-d)**2

        A = [D(p1,p2),D(p1,p3),D(p1,p4),D(p2,p3),D(p2,p4),D(p3,p4)]
        A.sort()

        print "A[0]=%.3f, A[5]=%.3f" %(A[0], A[5])
        return A[0]==A[1]==A[2]==A[3] and A[4]==A[5] and 2*A[0] == A[5] and A[0] > 0
