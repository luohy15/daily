from typing import List

def isNum(c):
    return ord(c) >= ord('0') and ord(c) <= ord('9')

def num(c):
    return ord(c) - ord('0')

class Solution(object):
    """
    time: O(n)
    space: O(1)
    """
    def myAtoi(self, s: str) -> int:
        start = False
        minus = False
        res = 0
        for c in s:
            if not start:
                if isNum(c):
                    start = True
                    res = num(c)
                elif c == "+":
                    start = True
                elif c == "-":
                    start = True
                    minus = True
                elif c == " ":
                    continue
                else:
                    break
            else:
                if not isNum(c):
                    break
                res *= 10
                res += num(c)
        res = -res if minus else res
        res = max(res, -2 ** 31)
        res = min(res, 2 ** 31 - 1)
        return res