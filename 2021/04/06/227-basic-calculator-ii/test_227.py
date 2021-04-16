import pytest

from main_227 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().calculate("100+3*4") == 112

def test2(Solution):
    assert Solution().calculate("3/2") == 1

def test3(Solution):
    assert Solution().calculate("14-3/2") == 13
