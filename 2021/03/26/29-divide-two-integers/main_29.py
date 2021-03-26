from typing import List

class Solution(object):
    """
    生成除数的2的n次方列表
    从大到小依次与被除数对比，如果可以减则减掉
    time: O(n)
    space: O(1)
    """
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1
        negative = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        power_list = []
        times = 1
        while divisor <= dividend:
            power_list.append([divisor, times])
            times += times
            divisor += divisor
        result = 0
        for power in reversed(power_list):
            if dividend >= power[0]:
                dividend -= power[0]
                result += power[1]
        return -result if negative else result