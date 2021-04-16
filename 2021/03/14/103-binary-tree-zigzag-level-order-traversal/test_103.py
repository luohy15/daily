import pytest

import sys
sys.path.append("./")
from lib.tree import arr2tree
from main_103 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    arr = [3,9,20,None,None,15,7]
    tree = arr2tree(arr)
    res = [
        [3],
        [20,9],
        [15,7]
    ]
    assert Solution().zigzagLevelOrder(tree) == res

def test2(Solution):
    arr = [1,2,3,4,None,None,5]
    tree = arr2tree(arr)
    res = [[1],[3,2],[4,5]]
    assert Solution().zigzagLevelOrder(tree) == res
