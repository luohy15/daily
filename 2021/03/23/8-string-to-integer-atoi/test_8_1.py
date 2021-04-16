import pytest

from main_8_1 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().parseInt("10") == 10
    assert Solution().parseInt("-10") == -10
    assert Solution().parseInt("+10") == 10
    assert Solution().parseInt(" +10") == 10
    assert Solution().parseInt(" 10") == 10
    assert Solution().parseInt(" 10 ") == 10
    assert Solution().parseInt("2147483647") == 2147483647
    assert Solution().parseInt("-2147483648") == -2147483648
    assert Solution().parseInt(" 10 0 ") == None
    assert Solution().parseInt("2147483648") == None
    assert Solution().parseInt("-2147483649") == None
    assert Solution().parseInt("aasdfasf10") == None
    assert Solution().parseInt("10aaasf") == None
