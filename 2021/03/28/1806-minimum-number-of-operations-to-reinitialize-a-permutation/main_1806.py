from typing import List

class Solution(object):
    """
    模拟，从1出发的元素需要回到1
    time: 待讨论
    space: O(1)
    """
    def reinitializePermutation(self, n: int) -> int:
        i = n / 2
        res = 1
        while i != 1:
            if i % 2 == 0:
                i = i / 2
            else:
                i = n / 2 + (i - 1) / 2
            res += 1
        return res
