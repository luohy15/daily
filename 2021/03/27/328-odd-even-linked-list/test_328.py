import pytest

from main_328 import Solution as Solution0
from main_328_1 import Solution as Solution1
import sys
sys.path.append("./")
from lib.list import arr2list, list2arr

@pytest.fixture(params=[Solution0, Solution1])
def Solution(request):
    return request.param

def test0(Solution):
    assert list2arr(Solution().oddEvenList(arr2list([1]))) == [1]

def test1(Solution):
    assert list2arr(Solution().oddEvenList(arr2list([1,2,3,4,5]))) == [1,3,5,2,4]

def test2(Solution):
    assert list2arr(Solution().oddEvenList(arr2list([1,2,3,4,5,6]))) == [1,3,5,2,4,6]

def test3(Solution):
    assert list2arr(Solution().oddEvenList(arr2list([]))) == []

def test4(Solution):
    assert list2arr(Solution().oddEvenList(arr2list([1,2]))) == [1,2]