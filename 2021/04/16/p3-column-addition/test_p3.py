import pytest

from main_p3 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test0(Solution):
    assert Solution().removeColumn("", "", "") == 0

def test1(Solution):
    assert Solution().removeColumn("123", "456", "579") == 0

def test2(Solution):
    assert Solution().removeColumn("12127", "45618", "51825") == 2

def test3(Solution):
    assert Solution().removeColumn("24", "32", "32") == 2

def test4(Solution):
    assert Solution().removeColumn("12299", "12299", "25598") == 1

def test5(Solution):
    assert Solution().removeColumn("128128", "157405", "986621") == 5

def test6(Solution):
    assert Solution().removeColumn("9", "9", "8") == 1
