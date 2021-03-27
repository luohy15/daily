import sys
sys.path.append("./")
from lib.list import ListNode

from typing import List
import heapq as hq

class Solution(object):
    """
    priority queue:
        find current minimal by priority queue, add to new list
    time: O(k * n * logk)
    space: O(k * n)
    """
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode()
        cur = dummy
        q = []
        for i, l in enumerate(lists):
            if l:
                hq.heappush(q, (l.val, i))
        while q:
            idx = hq.heappop(q)[1]
            l = lists[idx]
            cur.next = l
            cur = cur.next
            if l.next:
                lists[idx] = l.next
                hq.heappush(q, (l.next.val, idx))
        return dummy.next

