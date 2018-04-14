"""
https://www.hackerrank.com/challenges/coin-change/problem
Traditional coin-change problem: how many possible ways it is to change for n
units given m tokens?
"""

# Main idea: for each coin type, you can choose to either change it or not.
# Add up the sums of possible sub-problems.
# Be careful about the edge cases.
def calculate(n, m, mem, bases):
    if (n, m) in mem:
        return mem[n, m]
    if n == 0:
        ret = 1
    elif n < bases[0]:
        ret = 0
    elif m == 1:
        ret = int(n % bases[0] == 0)
    else:
        ret = 0
        nsum = n
        while nsum >= 0:
            ret += calculate(nsum, m-1, mem, bases)
            nsum -= bases[m-1]
    if (n, m) not in mem:
        mem[n, m] = ret
    return ret


if __name__ == '__main__':
    n, m = input().split(" ")
    n = int(n)
    m = int(m)
    temp = input().split(" ")
    bases = [int(b) for b in temp]
    bases = sorted(bases)

    mem = {}  # Money, coin_type_nums -> choice_nums
    ret = calculate(n, m, mem, bases)

    print(ret)
