from typing import List

class Solution(object):
    """
    最大升序子数组和
        参考53最大子序和
    time: O(n)
    space: O(n)
    """
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = nums[0]
        tmp = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                tmp += nums[i]
            else:
                tmp = nums[i]
            res = max(res, tmp)
        return res
