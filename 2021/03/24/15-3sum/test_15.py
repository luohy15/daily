import pytest

from main_15 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]

def test2(Solution):
    assert Solution().threeSum([-2,0,0,2,2]) == [[-2,0,2]]
