from typing import List

class Solution(object):
    """
    使用set维护字符集
    time: O(nlogn)
    space: O(C)
    其中C为字符集大小
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        r = 0
        res = 0
        chars = set()
        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                r += 1
                res = max(res, r - l)
            else:
                chars.remove(s[l])
                l += 1
        return res
