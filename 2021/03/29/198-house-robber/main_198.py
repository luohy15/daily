from typing import List

class Solution(object):
    """
    维护偷和不偷的最大金额，因为刚偷完不能马上再偷
    time: O(n)
    space: O(1)
    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        f = 0
        g = 0
        res = 0
        for n in nums:
            lf, lg = f, g
            f = max(lg + n, lf)
            g = max(lg, lf)
            res = max(res, f)
        return res
