import pytest

from main_101 import Solution as Solution0
from main_101 import Solution as Solution1
import sys
sys.path.append("./")
from lib.tree import arr2tree

@pytest.fixture(params=[Solution0, Solution1])
def Solution(request):
    return request.param

def test1(Solution):
    arr = [1,2,2,3,4,4,3]
    root = arr2tree(arr)
    assert Solution().isSymmetric(root) == True

def test2(Solution):
    arr = [1,2,2,None,3,None,3]
    root = arr2tree(arr)
    assert Solution().isSymmetric(root) == False

def test3(Solution):
    arr = [2,3,3,4,5,5,4,None,None,8,9,None,None,9,8]
    root = arr2tree(arr)
    assert Solution().isSymmetric(root) == False

def test4(Solution):
    arr = [1,0]
    root = arr2tree(arr)
    assert Solution().isSymmetric(root) == False
