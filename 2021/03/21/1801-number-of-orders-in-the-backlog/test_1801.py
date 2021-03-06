import pytest

from main_1801 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
    assert Solution().getNumberOfBacklogOrders(orders) == 6

def test2(Solution):
    orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
    assert Solution().getNumberOfBacklogOrders(orders) == 999999984
