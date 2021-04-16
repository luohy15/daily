from typing import List
import sys
sys.path.append("./")
from lib.list import ListNode

class Solution(object):
    """
    使用额外集合记录节点
    time: O(m+n)
    space: O(m)
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curr = headA
        nodes = set()
        while curr:
            nodes.add(curr)
            curr = curr.next
        curr = headB
        while curr:
            if curr in nodes:
                return curr
            curr = curr.next
        return None
