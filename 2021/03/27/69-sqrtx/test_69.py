import pytest

from main_69 import Solution as Solution0
from main_69_1 import Solution as Solution1

@pytest.fixture(params=[Solution0, Solution1])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().mySqrt(4) == 2

def test2(Solution):
    assert Solution().mySqrt(8) == 2