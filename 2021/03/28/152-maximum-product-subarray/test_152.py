import pytest

from main_152 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().maxProduct([2,3,-2,4]) == 6
