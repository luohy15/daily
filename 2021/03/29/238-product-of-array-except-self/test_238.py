import pytest

from main_238 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6]
