# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    """
    brute force:
        find current minimal, add to new list
    time: O(k * k * n)
    space: O(k * n)
    """
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode()
        cur = dummy
        
        while True:
            mi = 10 ** 5
            idx = -1
            for i, l in enumerate(lists):
                if l and l.val < mi:
                    mi = l.val
                    idx = i
            if idx == -1:
                break
            cur.next = lists[idx]
            cur = cur.next
            lists[idx] = lists[idx].next
        return dummy.next

