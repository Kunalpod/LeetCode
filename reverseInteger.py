# https://leetcode.com/problems/reverse-integer/

def reverse(self, x):
    lbound = -(2**31)
    ubound = (-1 * lbound) - 1
    rev = 0
    if x < 0:
        rev = -1 * int(str(-1 * x)[::-1])
    else:
        rev = int(str(x)[::-1])
    if rev < lbound or rev > ubound: return 0
    return rev
