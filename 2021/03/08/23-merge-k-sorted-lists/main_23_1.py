import sys
sys.path.append("./")
from lib.list import ListNode

def merge(lists, l, r):
    if l >= r:
        return None
    if l + 1 == r:
        return lists[l]
    mid = (l + r) // 2
    return mergeTwoLists(merge(lists, l, mid), merge(lists, mid, r))

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

class Solution(object):
    """
    divide and conquer:
        merge 2 list log k times
    time: O(k * n * logk)
    space: O(logk)
    """
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return merge(lists, 0, len(lists))
