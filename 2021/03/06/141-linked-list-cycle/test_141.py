import pytest

from main_141 import Solution
from main_141 import ListNode
import sys
sys.path.append("./")
from lib.list import arr2list, list2arr

def test1():
    arr = [3,2,0,-4]
    _list = arr2list(arr)
    cur = _list
    dst = cur.next
    while cur.next:
        cur = cur.next
    src = cur
    src.next = dst
    assert Solution().hasCycle(_list) == True

def test2():
    arr = [1,2]
    _list = arr2list(arr)
    _list.next.next = _list
    assert Solution().hasCycle(_list) == True

def test3():
    _list = ListNode(1)
    assert Solution().hasCycle(_list) == False