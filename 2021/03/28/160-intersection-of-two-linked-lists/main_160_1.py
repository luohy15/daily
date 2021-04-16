from typing import List
import sys
sys.path.append("./")
from lib.list import ListNode

class Solution(object):
    """
    各自走一遍对方的路，总路程相同就可以相遇了
    time: O(m+n)
    space: O(1)
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        ca = headA
        cb = headB
        while ca != cb:
            ca = ca.next if ca else headB
            cb = cb.next if cb else headA
        return ca
