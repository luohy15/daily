import unittest

from main_83 import Solution
from main_83 import ListNode

def arr2list(arr):
    dummy = ListNode()
    cur = dummy
    for a in arr:
        cur.next = ListNode(a)
        cur = cur.next
    return dummy.next

def list2arr(_list):
    arr = []
    cur = _list
    while cur:
        arr.append(cur.val)
        cur = cur.next
    return arr

def checkSolution(arr_in, arr_out):
    list_in = arr2list(arr_in)
    list_out = Solution().deleteDuplicates(list_in)
    cur = list_out
    for a in arr_out:
        assert cur.val == a
        cur = cur.next
    assert cur == None

def test1():
    l = [1,1,2]
    rl = [1,2]
    checkSolution(l, rl)

def test2():
    l = [1,1,2,3,3]
    rl = [1,2,3]
    checkSolution(l, rl)