import pytest

from main_83 import Solution
import sys
sys.path.append("./")
from lib.list import ListNode, arr2list, list2arr

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
