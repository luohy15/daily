import sys
sys.path.append("./")
from lib.list import ListNode

class Solution(object):
    """
    stack:
        use stack to reverse list
    time: O(n)
    space: O(k)
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
            # push k group to stack
            stack = []
            for i in range(k):
                if ptr:
                    stack.append(ptr)
                    ptr = ptr.next
                else:
                    return dummy.next
            tmp = ptr
            # pop from stack
            for i in range(k):
                curr_dummy.next = stack.pop()
                curr_dummy = curr_dummy.next
            curr_dummy.next = tmp
        return dummy.next
