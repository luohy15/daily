import pytest

from main_29 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().divide(10, 3) == 3

def test2(Solution):
    assert Solution().divide(7, -3) == -2

def test3(Solution):
    assert Solution().divide(1, 1) == 1

def test4(Solution):
    assert Solution().divide(-2 ** 31, -1) == 2 ** 31 - 1
