from typing import List
import sys
sys.path.append("./")
from lib.list import ListNode

class Solution(object):
    """
    两数相加
        注意进位即可
    time: O(n)
    space: O(1)
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode()
        curr = dummy
        while l1 or l2:
            c1 = l1.val if l1 else 0
            c2 = l2.val if l2 else 0
            s = int(c1) + int(c2) + carry
            curr.next = ListNode(s % 10)
            carry = s // 10
            curr = curr.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry:
            curr.next = ListNode(carry)
        return dummy.next