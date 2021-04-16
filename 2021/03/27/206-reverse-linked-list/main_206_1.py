from typing import List
import sys
sys.path.append("./")
from lib.list import ListNode

class Solution(object):
    """
    反转链表
        head->next->
        head->next<-
        head<-next<-
    time: O(n)
    space: O(1)
    """
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        newhead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newhead
