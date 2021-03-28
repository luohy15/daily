import pytest

from main_160 import Solution as Solution0
from main_160_1 import Solution as Solution1
import sys
sys.path.append("./")
from lib.list import arr2list, list2arr

@pytest.fixture(params=[Solution0, Solution1])
def Solution(request):
    return request.param

def test1(Solution):
    la = arr2list([4,1])
    lb = arr2list([5,0,1,8,4,5])
    ca = la
    ca = ca.next
    cb = lb
    cb = cb.next
    cb = cb.next
    cb = cb.next
    ca.next = cb
    assert Solution().getIntersectionNode(la, lb).val == 8

def test2(Solution):
    la = arr2list([0,9,1,2,4])
    lb = arr2list([3])
    ca = la
    ca = ca.next
    ca = ca.next
    ca = ca.next
    cb = lb
    cb.next = ca
    assert Solution().getIntersectionNode(la, lb).val == 2

def test3(Solution):
    la = arr2list([2,6,4])
    lb = arr2list([1,5])
    assert Solution().getIntersectionNode(la, lb) == None