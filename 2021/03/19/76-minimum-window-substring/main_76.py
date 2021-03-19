from typing import List

class Solution(object):
    """
    滑动窗口：
        延伸：如果当前窗口子串不能覆盖t，则右指针延伸
        收缩：如果当前窗口子串已覆盖t，则左指针收缩
    time: O(len(s) * C)
    space: O(C)
    其中C为字符集大小
    """
    def cover(self, mt, ms):
        for key in mt.keys():
            if key not in ms or ms[key] < mt[key]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        l = len(s)
        mi = l + 1
        res = ""
        mt = {}
        for tt in t:
            if tt in mt:
                mt[tt] += 1
            else:
                mt[tt] = 1
        i = 0
        j = 0
        ms = {}
        while j < l:
            # 没有覆盖，需要延伸
            while not self.cover(mt, ms) and j < l:
                if s[j] in ms:
                    ms[s[j]] += 1
                else:
                    ms[s[j]] = 1
                j += 1
            # 保持覆盖，缩小窗口
            while self.cover(mt, ms):
                if j - i < mi:
                    mi = j - i
                    res = s[i:j]
                ms[s[i]] -= 1
                i += 1
        return res