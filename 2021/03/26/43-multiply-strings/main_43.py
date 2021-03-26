from typing import List

class Solution(object):
    """
    竖式乘法
        把i，j位置的数相乘后累积到i+j位置
        统一处理进位
    time: O(1)
    space: O(1)
    """
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        arr = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                arr[i+j] = arr[i+j] + int(num1[i]) * int(num2[j])
        carry = 0
        res = ""
        for i in range(len(num1) + len(num2) - 2, -1, -1):
            arr[i] = arr[i] + carry
            carry = arr[i] // 10
            res += str(arr[i] % 10)
        if carry:
            res += str(carry)
        return res[::-1]
        