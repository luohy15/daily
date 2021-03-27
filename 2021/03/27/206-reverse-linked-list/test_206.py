import pytest

from main_206 import Solution as Solution0
from main_206_1 import Solution as Solution1
import sys
sys.path.append("./")
from lib.list import arr2list, list2arr

@pytest.fixture(params=[Solution0, Solution1])
def Solution(request):
    return request.param

def test1(Solution):
    arr = [1,2,3,4,5]
    assert list2arr(Solution().reverseList(arr2list(arr))) == [5,4,3,2,1]
