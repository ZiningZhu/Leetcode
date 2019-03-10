class Solution:
    def clumsy(self, N: int) -> int:
        res = 0
        tmp = 0
        last_n = -1

        for i in range(0, N, 4):

            last_n = N-i
            #print("last_n:" + str(last_n))
            if last_n - 4 < 0:
                break
            tmp = (N - i) * (N - i - 1) // (N - i - 2)
            if i == 0:
                res = tmp + (N - i - 3)
            else:
                res = res - tmp + (N - i - 3)
            #print("tmp:" + str(tmp))

        # Handle the last few tokens
        if N == 3:
            res = 6
        elif N == 2:
            res = 2
        elif N == 1:
            res = 1
        else:
            if last_n == 3:
                res -= 6
            elif last_n == 2:
                res -= 2
            elif last_n == 1:
                res -= 1
            elif last_n == -1:
                res = 0
            else:
                pass
        return res

        
