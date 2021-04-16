class Solution(object):
    """
    brute force:
        remove cur.next when cur.val == cur.next.val
    time: O(n)
    space: O(1)
    """
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                # delete cur.next
                cur.next = cur.next.next
            else:
                # move cur to next
                cur = cur.next
        return head
