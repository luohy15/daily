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
        while odd:
            # 连接odd
            if odd.next:
                odd.next = odd.next.next
            # 连接even
            if odd.next:
                odd = odd.next
                even.next = odd.next
                even = even.next
            else:
                odd.next = evenHead
                break
        return head