from typing import List
from collections import Counter

class Solution(object):
    """
    使用Python Counter
    time: O(n)
    space: O(n)
    """
    def frequencySort(self, s: str) -> str:
        return "".join([i * j for i, j in Counter(s).most_common()])
