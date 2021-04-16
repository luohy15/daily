import pytest

import sys
sys.path.append("./")
from lib.tree import arr2tree
from main_129 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    root = [1,2,3]
    assert Solution().sumNumbers(arr2tree(root)) == 25

def test2(Solution):
    root = [4,9,0,5,1]
    assert Solution().sumNumbers(arr2tree(root)) == 1026

def test3(Solution):
    root = [4,9,0,None,5,1]
    assert Solution().sumNumbers(arr2tree(root)) == 896
