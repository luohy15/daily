class Solution(object):
    """
    brute force:
        use two pointer: slow and fast
        if list has cycle, slow and fast must meet
    time: O(n)
    space: O(1)
    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
