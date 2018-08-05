class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # Decode directly until length reaches K
        # Memory limit exceeded
        """
        buff = ""
        for i in range(len(S)):
            try:
                rep = int(S[i])
                if len(buff) * rep < K:
                    buff = "".join([buff] * rep)
                else:
                    return buff[(K-1) % len(buff)]
            except ValueError:
                buff = buff + S[i]
                if len(buff) == K:
                    return S[i]
        """

        # Forward-backward solution
        length = 0
        i = 0
        for i in range(len(S)):
            if S[i].isdigit():
                rep = int(S[i])
                length *= rep
                if length >= K:
                    break
            else:
                length += 1

        for j in range(i, -1, -1):
            if S[j].isdigit():
                rep = int(S[j])
                length /= rep
                K %= length
            else:
                if K == 0 or length == K:
                    return S[j]
                length -= 1


        
