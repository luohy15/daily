from typing import List

class Solution(object):
    """
    维护最大乘积和最小乘积（因为有负数，所以最大乘积可能由最小乘积得来）
    time: O(n)
    space: O(1)
    """
    def maxProduct(self, nums: List[int]) -> int:
        ma = nums[0]
        mi = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            ta, ti = ma, mi
            ma = max(ta * nums[i], max(ti * nums[i], nums[i]))
            mi = min(ta * nums[i], min(ti * nums[i], nums[i]))
            res = max(res, ma)
        return res
