from typing import List

class Solution(object):
    """
    最大升序子数组和
        每个位置，找到最右边
    time: O(n)
    space: O(n)
    """
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = 0
        l = len(nums)
        for i in range(l):
            tmp = nums[i]
            curr = i + 1
            while curr < l and nums[curr] > nums[curr - 1]:
                tmp += nums[curr]
                curr += 1
            res = max(res, tmp)
        return res

class Solution1(object):
    """
    最大升序子序列和
        map维护[最后一个数,子数组和]
        新加入一个元素
        更新此数组
        map values取max
    time: O(n)
    space: O(n)
    """
    def maxAscendingSum(self, nums: List[int]) -> int:
        ma = {}
        for num in nums:
            keys = list(filter(lambda key: ma[key] < num, ma.keys()))
            maxx = 0
            if keys:
                maxx = max(list(map(lambda key: ma[key], keys)))
            ma[num] = maxx + num
            print(ma)
        return max(ma.values())
