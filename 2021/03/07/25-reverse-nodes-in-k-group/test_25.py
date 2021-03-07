import unittest

from main_25 import ListNode
from main_25 import Solution
from main_25_1 import Solution
from main_25_2 import Solution

def test1():
    checkFunc([1,2,3,4,5], [2,1,4,3,5], Solution().reverseKGroup, 2)

def test2():
    checkFunc([1,2,3,4,5], [3,2,1,4,5], Solution().reverseKGroup, 3)

def test3():
    checkFunc([1,2,3,4,5], [1,2,3,4,5], Solution().reverseKGroup, 1)

def test4():
    checkFunc([1], [1], Solution().reverseKGroup, 1)

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

def checkFunc(arr_in, arr_out, func, k):
    list_in = arr2list(arr_in)
    list_out = func(list_in, k)
    cur = list_out
    for a in arr_out:
        assert cur.val == a
        cur = cur.next
    assert cur == None