import pytest

from main_43 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().multiply("11", "11") == "121"

def test2(Solution):
    assert Solution().multiply("11", "10") == "110"

def test3(Solution):
    assert Solution().multiply("8", "9") == "72"

def test4(Solution):
    assert Solution().multiply("123", "456") == "56088"

def test5(Solution):
    assert Solution().multiply("9133", "0") == "0"