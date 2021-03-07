# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    """
    simulate:
        reverse list by maintain two pointer: src & dst
    time: O(n)
    space: O(1)
    """
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode()
        curr_dummy = dummy
        curr_dummy.next = head
        ptr = head
        while ptr:
            # find k group with initial src and dst
            src = ptr
            for i in range(k):
                if ptr:
                    ptr = ptr.next
                else:
                    return dummy.next
            dst = ptr
            # src -> dst
            # shift src and dst
            for i in range(k):
                tmp = src.next
                src.next = dst
                dst = src
                src = tmp
            # curr_dummy -> dst
            curr_dummy.next = dst
            for i in range(k):
                curr_dummy = curr_dummy.next
        return dummy.next
