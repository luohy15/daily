import pytest

from main_5709 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().maxAscendingSum([10,20,30,5,10,50]) == 65
    assert Solution().maxAscendingSum([10,20,30,40,50]) == 150
    assert Solution().maxAscendingSum([12,17,15,13,10,11,12]) == 33
    assert Solution().maxAscendingSum([100,10,1]) == 100
