from typing import List

class Solution(object):
    """
    使用map, list, join, filter, set
    time: O(n)
    space: O(n)
    """
    def numDifferentIntegers(self, word: str) -> int:
        return len(set(map(lambda x: int(x), filter(lambda x: x.isnumeric(), "".join(list(map(lambda x: x if x.isnumeric() else " ", word))).split(" ")))))
