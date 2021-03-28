from typing import List
import heapq as hq
from functools import reduce

def count(ma, n):
    if n in ma:
        ma[n] += 1
    else:
        ma[n] = 1
    return ma

class Solution(object):
    """
    heap:
        use heapq's nlargest method
    time: O(n * logk)
    space: O(n)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ma = reduce(count, nums, {})
        return list(map(lambda r: r[1], hq.nlargest(k, map(lambda key: (ma[key], key), ma.keys()))))