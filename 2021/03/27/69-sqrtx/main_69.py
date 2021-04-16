from typing import List

class Solution(object):
    """
    二分查找
        保持 mid * mid <= x 性质成立
    time: O(logn)
    space: O(1)
    """
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
