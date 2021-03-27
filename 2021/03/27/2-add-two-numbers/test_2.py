import pytest

from main_2 import Solution as Solution0
import sys
sys.path.append("./")
from lib.list import arr2list, list2arr

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert list2arr(Solution().addTwoNumbers(arr2list([2,4,3]), arr2list([5,6,4]))) == [7,0,8]

def test2(Solution):
    assert list2arr(Solution().addTwoNumbers(arr2list([0]), arr2list([0]))) == [0]

def test3(Solution):
    assert list2arr(Solution().addTwoNumbers(arr2list([9,9,9,9,9,9,9]), arr2list([9,9,9,9]))) == [8,9,9,9,0,0,0,1]