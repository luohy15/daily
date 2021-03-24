from typing import List

class Solution(object):
    """
    3sum
        排序
        双指针：枚举第一个数，剩下两个数使用双指针判断移动
        避免重复：如果第一个数和第二个数已经枚举过，则continue
        剪枝条件：第一个数>0或者第三个数<0可以提前退出
    time: O(n ** 2)
    space: O(logn)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        if nums[0] > 0 or nums[-1] < 0:
            return []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        return res