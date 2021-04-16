import pytest

from main_94 import Solution as Solution0
from main_94_1 import Solution as Solution1
import sys
sys.path.append("./")
from lib.tree import arr2tree

@pytest.fixture(params=[Solution0, Solution1])
def Solution(request):
    return request.param

def test1(Solution):
    arr = [1,None,2,None,None,3]
    root = arr2tree(arr)
    assert Solution().inorderTraversal(root) == [1,3,2]

def test2(Solution):
    arr = [1,None,2]
    root = arr2tree(arr)
    assert Solution().inorderTraversal(root) == [1,2]

def test3(Solution):
    arr = []
    root = arr2tree(arr)
    assert Solution().inorderTraversal(root) == []
