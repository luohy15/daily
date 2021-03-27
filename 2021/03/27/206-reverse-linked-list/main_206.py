from typing import List
import sys
sys.path.append("./")
from lib.list import ListNode

class Solution(object):
    """
    反转链表
        dst  src->next
        dst<-src  next
             dst  src  next
    time: O(n)
    space: O(1)
    """
    def reverseList(self, head: ListNode) -> ListNode:
        dst = None
        src = head
        while src:
            tmp = src.next
            src.next = dst
            dst = src
            src = tmp
        return dst
