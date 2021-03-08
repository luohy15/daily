import pytest


from main_21 import ListNode
from main_21 import Solution as Solution0
from main_21_1 import Solution as Solution1
import sys
sys.path.append("./")
from lib.list import arr2list, list2arr

@pytest.fixture(params=[Solution0, Solution1])
def Solution(request):
    return request.param

def test1(Solution):
    l1 = arr2list([1,2,4])
    l2 = arr2list([1,3,4])
    assert list2arr(Solution().mergeTwoLists(l1, l2)) == [1, 1, 2, 3, 4, 4]

def test2(Solution):
    l1 = None
    l2 = None
    l = Solution().mergeTwoLists(l1, l2)
    assert l == None

def test3(Solution):
    l1 = None
    l2 = ListNode(0)
    l = Solution().mergeTwoLists(l1, l2)
    assert l.val == 0
    assert l.next == None
