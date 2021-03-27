from typing import List

class Solution(object):
    """
    二进制位对应子集
    time: O(n * 2 ** n)
    space: O(1)
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(2 ** len(nums)):
            s = bin(i)[2:].zfill(len(nums))[::-1]
            ress = []
            for j in range(len(nums)):
                if s[j] == "1":
                    ress.append(nums[j])
            res.append(ress)
        return res