from typing import List

class Solution(object):
    """
    牛顿迭代 xi = x0 - f(x0) / f'(x0)
    time: O(logn)
    space: O(1)
    """
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        C, x0 = float(x), float(x)
        while True:
            fx0 = x0 * x0 - C
            fx01 = 2 * x0
            xi = x0 - fx0 / fx01
            if abs(xi - x0) < 1e-7:
                break
            x0 = xi
        
        return int(x0)
