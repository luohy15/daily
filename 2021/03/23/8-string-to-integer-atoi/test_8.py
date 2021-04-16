import pytest

from main_8 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().myAtoi("42") == 42

def test2(Solution):
    assert Solution().myAtoi("        -42") == -42

def test3(Solution):
    assert Solution().myAtoi("4193 with words") == 4193

def test4(Solution):
    assert Solution().myAtoi("words and 987") == 0

def test5(Solution):
    assert Solution().myAtoi("-91283472332") == -2147483648

def test6(Solution):
    assert Solution().myAtoi("0010") == 10
