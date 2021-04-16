from typing import List

class Solution(object):
    """
    乘积=当前数左边乘积*当前数右边乘积
    先赋值后累乘，就可以排除掉当前数
    time: O(n)
    space: O(1)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            res[i] = product
            product *= nums[i]
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= product
            product *= nums[i]
        return res
