import pytest

from main_415 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().addStrings("234", "567") == "801"

def test2(Solution):
    assert Solution().addStrings("1234567", "8") == "1234575"

def test3(Solution):
    assert Solution().addStrings("333", "667") == "1000"