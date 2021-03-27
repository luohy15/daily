import pytest

from main_23 import Solution as Solution0
from main_23_1 import Solution as Solution1
from main_23_2 import Solution as Solution2
from main_23_3 import Solution as Solution3
import sys
sys.path.append("./")
from lib.list import ListNode, arr2list, list2arr

@pytest.fixture(params=[Solution0, Solution1, Solution2, Solution3])
def Solution(request):
    return request.param

def test1(Solution):
    lists = [[1,4,5],[1,3,4],[2,6]]
    li = []
    for l in lists:
        li.append(arr2list(l))
    assert list2arr(Solution().mergeKLists(li)) == [1,1,2,3,4,4,5,6]

def test2(Solution):
    lists = []
    assert list2arr(Solution().mergeKLists(lists)) == []

def test3(Solution):
    lists = [[]]
    assert list2arr(Solution().mergeKLists(lists)) == []
