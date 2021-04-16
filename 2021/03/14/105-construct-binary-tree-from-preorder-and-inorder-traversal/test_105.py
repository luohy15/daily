import pytest

from main_105 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    assert Solution().arr2tree(preorder, inorder).val == 3

def test2(Solution):
    preorder = [1,2]
    inorder = [2,1]
    assert Solution().arr2tree(preorder, inorder).val == 1
