from typing import List

class Solution(object):
    """
    quick sort:
        one line version
    time: O(nlogn)
    space: O(logn)
    """
    def sortArray(self, nums: List[int]) -> List[int]:
        quicksort = lambda l: quicksort([i for i in l[1:] if i < l[0]]) + [l[0]] + quicksort([j for j in l[1:] if j >= l[0]]) if l else []
        return quicksort(nums)