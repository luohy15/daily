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
        cnt = 0
        # 把0扫到左边
        for i in range(l):
            if nums[i] == 0:
                nums[i], nums[cnt] = nums[cnt], nums[i]
                cnt += 1
        # 把2扫到右边
        cnt = 0
        for i in range(l - 1, -1, -1):
            if nums[i] == 2:
                nums[i], nums[l - 1 - cnt] = nums[l - 1 - cnt], nums[i]
                cnt += 1