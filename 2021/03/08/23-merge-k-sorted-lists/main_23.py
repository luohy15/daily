import sys
sys.path.append("./")
from lib.list import ListNode

def mergeTwoLists(l1, l2):
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

# Time Limit Exceeded
class Solution(object):
    """
    brute force:
        merge 2 list k times
    time: O(k**2 * n)
    space: O(1)
    """
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return
        dummy = ListNode()
        dummy.next = lists[0]
        for i in lists[1:]:
            dummy.next = mergeTwoLists(dummy.next, i)
        return dummy.next
