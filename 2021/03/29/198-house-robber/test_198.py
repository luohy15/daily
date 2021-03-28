import pytest

from main_198 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().rob([1,2,3,1]) == 4
    assert Solution().rob([2,7,9,3,1]) == 12

def test2(Solution):
    assert Solution().rob([2,1,1,2]) == 4
