from typing import List

class Solution(object):
    """
    在括号前后加上空格再split即可获得括号对
    time: O(n)
    space: O(n)
    """
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {}
        for k in knowledge:
            d[k[0]] = k[1]
        return "".join(list(map(lambda x: x if x[0] != "(" else d[x[1:-1]] if x[1:-1] in d else "?", s.replace("(", " (").replace(")", ") ").split())))
