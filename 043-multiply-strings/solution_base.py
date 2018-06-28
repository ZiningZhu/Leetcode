# Question: input num1, num2, output the product of them
# A TLE Solution: exercise in position-wise manipulation of multi-digit multiplications

class Solution(object):
    def mult_(self, a, b):
        m = int(a) * int(b)
        carry = str(m / 10)
        result = str(m % 10)
        return carry, result

    def add_(self, a, b):
        r = int(a) + int(b)
        result = str(r % 10)
        carry = str(r / 10)
        return carry, result

    def add(self, a, b):
        if len(a) < len(b):
            a, b = b, a
        b = b.rjust(len(a), '0')
        res = [0] * (1+len(a))
        for i in range(len(a), 0, -1):
            carry, result = self.add_(a[i-1], b[i-1])
            additional_carry, nres = self.add_(result, res[i])
            _, res[i-1] = self.add_(carry, additional_carry)
            res[i] = nres

        ret = "".join(res).lstrip('0')
        if len(ret) == 0:
            return "0"
        else:
            return ret

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = "0"
        for i in range(len(num1)-1, -1, -1):
            step_res = "0"  # num1[i] * num2
            mult_res = [0] * (1+len(num2))
            for j in range(len(num2), 0, -1):
                carry, result = self.mult_(num1[i], num2[j-1])
                additional_carry, nres = self.add_(mult_res[j], result)
                _, ncar = self.add_(carry, additional_carry)
                mult_res[j] = nres
                mult_res[j-1] = ncar

            mult_res_int = "".join(mult_res)
            step_res = self.add(step_res, mult_res_int)
            step_res = step_res + "0" * (len(num1) - i - 1)

            res = self.add(res, step_res)

        ret = res.lstrip('0')
        if len(ret) == 0:
            ret = "0"
        return ret
