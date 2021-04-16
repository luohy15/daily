from typing import List

class Solution(object):
    """
    word字符排序完当做key
    time: O(klogk * n)
    space: O(nk)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ma = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss in ma:
                ma[ss].append(s)
            else:
                ma[ss] = [s]
        return list(ma.values())
