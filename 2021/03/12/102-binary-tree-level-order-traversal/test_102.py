import pytest

import sys
sys.path.append("./")
from lib.tree import arr2tree
from main_102 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    arr = [3,9,20,None,None,15,7]
    tree = arr2tree(arr)
    res =[
        [3],
        [9,20],
        [15,7]
    ]
    assert Solution().levelOrder(tree) == res
