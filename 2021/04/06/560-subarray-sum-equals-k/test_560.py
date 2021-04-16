import pytest

from main_560 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().subarraySum([1,2,2,3], 5) == 2

def test2(Solution):
    assert Solution().subarraySum([1,1,1], 2) == 2
