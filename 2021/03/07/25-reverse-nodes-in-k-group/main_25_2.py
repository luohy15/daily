# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    """
    recursive:
        use recursive method to reverse remaining parts
    time: O(n)
    space: O(n)
    """
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        ptr = head
        for i in range(k):
            if ptr:
                ptr = ptr.next
            else:
                return head
        # reverse remaining parts
        ptr = self.reverseKGroup(ptr, k)
        # reverse k group
        src = head
        dst = ptr
        for i in range(k):
            tmp = src.next
            src.next = dst
            dst = src
            src = tmp
        return dst
