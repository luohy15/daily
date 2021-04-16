from typing import List

class Solution(object):
    """
    竖式加法
        对较短的数字进行补0操作
    time: O(n)
    space: O(1)
    """
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        res = ''
        for i in range(max(len(num1), len(num2))):
            c1 = num1[len(num1) - 1 - i] if i <= len(num1) - 1 else 0
            c2 = num2[len(num2) - 1 - i] if i <= len(num2) - 1 else 0
            s = int(c1) + int(c2) + carry
            res += str(s % 10)
            carry = s // 10
        if carry:
            res += '1'
        return res[::-1]
