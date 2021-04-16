from typing import List

class Solution(object):
    """
    前缀和+哈希
    time: O(n)
    space: O(n)
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        pre = 0
        res = 0
        for n in nums:
            pre += n
            if pre - k in mp:
                res += mp[pre - k]
            if pre in mp:
                mp[pre] += 1
            else:
                mp[pre] = 1
        return res
