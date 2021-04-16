import pytest

import sys
sys.path.append("./")
from lib.tree import arr2tree, TreeNode
from main_236 import Solution as Solution0
from main_236_1 import Solution as Solution1

@pytest.fixture(params=[Solution0, Solution1])
def Solution(request):
    return request.param

def test1(Solution):
    root = [3,5,1,6,2,0,8,None,None,7,4]
    assert Solution().lowestCommonAncestor(arr2tree(root), TreeNode(5), TreeNode(1)).val == 3
