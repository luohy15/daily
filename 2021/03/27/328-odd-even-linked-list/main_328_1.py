from typing import List
import sys
sys.path.append("./")
from lib.list import ListNode

class Solution(object):
    """
    模拟连接odd和even
    time: O(n)
    space: O(1)
    """
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        evenHead = head.next
        even = evenHead
        while even and even.next:
            # 连接odd
            odd.next = even.next
            odd = odd.next
            # 连接even
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
