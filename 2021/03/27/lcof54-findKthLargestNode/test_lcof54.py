import pytest

from main_lcof54 import Solution as Solution0
import sys
sys.path.append("./")
from lib.tree import tree2arr, arr2tree

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().kthLargest(arr2tree([3,1,4,None,2]),1) == 4

def test2(Solution):
    assert Solution().kthLargest(arr2tree([5,3,6,2,4,None,None,1]),3) == 4