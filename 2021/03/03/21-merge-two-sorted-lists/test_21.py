import unittest

from main_21 import Solution
from main_21_1 import Solution
from main_21 import ListNode

def test1():
    l1 = ListNode(1)
    l1n = ListNode(2)
    l1nn = ListNode(4)
    l1.next = l1n
    l1n.next = l1nn
    l2 = ListNode(1)
    l2n = ListNode(3)
    l2nn = ListNode(4)
    l2.next = l2n
    l2n.next = l2nn
    l = Solution().mergeTwoLists(l1, l2)
    res = [1, 1, 2, 3, 4, 4]
    for i in range(6):
        assert l.val == res[i]
        l = l.next
    assert l == None

def test2():
    l1 = None
    l2 = None
    l = Solution().mergeTwoLists(l1, l2)
    assert l == None

def test3():
    l1 = None
    l2 = ListNode(0)
    l = Solution().mergeTwoLists(l1, l2)
    assert l.val == 0
    assert l.next == None