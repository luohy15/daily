import pytest

from main_226 import Solution as Solution0
import sys
sys.path.append("./")
from lib.tree import arr2tree, tree2arr

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    arr = [4,2,7,1,3,6,9]
    root = arr2tree(arr)
    assert tree2arr(Solution().invertTree(root)) == [4,7,2,9,6,3,1]

def test2(Solution):
    arr = [1,2]
    root = arr2tree(arr)
    assert tree2arr(Solution().invertTree(root)) == [1,None,2]