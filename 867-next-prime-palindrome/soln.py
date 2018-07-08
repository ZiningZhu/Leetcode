# Question: next prime palindrome
# 81/87 test cases passed; remaining TLE. But there are some good tricks to know

class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = N
        while True:
            ds = self.get_digits(n)
            if n > 11 and len(ds) % 2 == 0:
                # Another trick.
                # See proof at https://math.stackexchange.com/questions/697096/prove-that-any-palindrome-with-an-even-number-of-digits-is-divisible-by-11
                n += 1
                continue
            else:
                if self.is_palindrome(n) and self.is_prime(n):
                    return n
                n += 1

    def is_prime(self, x):
        # Boundary conditions, and optimization trick
        if x<30:
            return x in [2,3,5,7,11,13,17,19,23,29]
        if x % 2 == 0:
            return False
        if x % 3 == 0:
            return False
        for p in range(5, x, 6):
            if p ** 2 > x:
                return True
            if (x % p == 0) or (x % (p+2) == 0):
                return False
        return False

    def is_palindrome(self, x):
        # log(10) runtime
        ds = self.get_digits(x)

        for i in range(len(ds) / 2):
            if ds[i] != ds[len(ds) - i - 1]:
                return False
        return True

    def get_digits(self, x):
        n = x
        ds = []
        while n > 0:
            ds.append(n % 10)
            n /= 10
        return ds
