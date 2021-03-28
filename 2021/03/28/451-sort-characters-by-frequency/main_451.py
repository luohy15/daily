from typing import List
from functools import reduce
import heapq as hq

def count(ma, n):
    if n in ma:
        ma[n] += 1
    else:
        ma[n] = 1
    return ma

class Solution(object):
    """
    使用堆获得有序元素
    time: O(n)
    space: O(n)
    """
    def frequencySort(self, s: str) -> str:
        ma = reduce(count, s, {})
        return "".join(list(map(lambda r: r[1] * r[0], hq.nlargest(len(s), map(lambda key: (ma[key], key), ma.keys())))))
