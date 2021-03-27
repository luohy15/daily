import pytest

from main_42 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
