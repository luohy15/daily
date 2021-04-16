from typing import List

def parseChar(char):
    return ord(char) - ord('0')

def isNum(char):
    return ord(char) >= ord('0') and ord(char) <= ord('9')

class Solution(object):
    """
    time: O(n)
    space: O(1)
    """
    def parseInt(self, s):
        minus = False
        start = False
        space = False
        res =  0
        for char in s:
            if not start:
                # 如果还没开始累加
                if isNum(char):
                    start = True
                    res = parseChar(char)
                elif char == "+":
                    start = True
                elif char == "-":
                    start = True
                    minus = True
                elif char == " ":
                    continue
                else:
                    return None
            else:
                # 如果开始累加，要求字符都是数字
                if not isNum(char):
                    if char == " ":
                        space = True
                        continue
                    return None
                if space:
                    return None
                res *= 10
                res += parseChar(char)
        res = -res if minus else res
        if res >= 2147483648:
            return None
        if res < -2147483648:
            return None
        return res
