from typing import List

class Solution(object):
    """
    把所有0交换到左边
    把所有2交换到右边
    time: O(n)
    space: O(1)
    """
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        p0 = 0
        p2 = l - 1
        i = 0
        while i <= p2:
            while i <= p2 and nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
            if nums[i] == 0:
                nums[i], nums[p0] = nums[p0], nums[i]
                p0 += 1
            i += 1
