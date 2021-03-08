import pytest

from main_25 import ListNode
from main_25 import Solution as Solution0
from main_25_1 import Solution as Solution1
from main_25_2 import Solution as Solution2
from lib.list import arr2list, list2arr

@pytest.fixture(params=[Solution0, Solution1, Solution2])
def Solution(request):
    return request.param

def test1(Solution):
    checkFunc([1,2,3,4,5], [2,1,4,3,5], Solution().reverseKGroup, 2)

def test2(Solution):
    checkFunc([1,2,3,4,5], [3,2,1,4,5], Solution().reverseKGroup, 3)

def test3(Solution):
    checkFunc([1,2,3,4,5], [1,2,3,4,5], Solution().reverseKGroup, 1)

def test4(Solution):
    checkFunc([1], [1], Solution().reverseKGroup, 1)

def checkFunc(arr_in, arr_out, func, k):
    list_in = arr2list(arr_in)
    list_out = func(list_in, k)
    cur = list_out
    for a in arr_out:
        assert cur.val == a
        cur = cur.next
    assert cur == None