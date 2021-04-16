import sys
sys.path.append("./")
from lib.list import ListNode

class Solution(object):
    """
    brute force:
        while l1 and l2: merge smaller one
        when finished: merge remaining all
    time: O(n+m)
    space: O(1)
    """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode()
        tmp = res
        while l1 and l2:
            if l1.val <= l2.val:
                tmp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tmp.next = ListNode(l2.val)
                l2 = l2.next
            tmp = tmp.next
        if l1:
            tmp.next = l1
        else:
            tmp.next = l2
        return res.next
