from typing import List

class Solution(object):
    """
    投票算法：
    time: O(n)
    space: O(1)
    """
    def majorityElement(self, nums: List[int]) -> int:
        cur = nums[0]
        cnt = 1
        for n in nums[1:]:
            if cur == n:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    cur = n
                    cnt = 1
        return cur
