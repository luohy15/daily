import sys
sys.path.append("./")
from lib.binarysearch import lower_bound

class Solution(object):
    """
    greedy & binary search:
        keep every element in LIS as small as possible (more likely to grow)
        find lower_bound for candidate, then overwritten
    time: O(nlogn)
    space: O(n)
    """
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lis = []
        for n in nums:
            if not lis or n > lis[-1]:
                lis.append(n)
            else:
                lis[lower_bound(lis, n)] = n
        return len(lis)