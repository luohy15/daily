import pytest

from main_98 import Solution as Solution0
from main_98_1 import Solution as Solution1
import sys
sys.path.append("./")
from lib.tree import arr2tree

@pytest.fixture(params=[Solution0, Solution1])
def Solution(request):
    return request.param

def test0(Solution):
    arr = []
    root = arr2tree(arr)
    assert Solution().isValidBST(root) == True

def test1(Solution):
    arr = [2,1,3]
    root = arr2tree(arr)
    assert Solution().isValidBST(root) == True

def test2(Solution):
    arr = [5,1,4,None,None,3,6]
    root = arr2tree(arr)
    assert Solution().isValidBST(root) == False