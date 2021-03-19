import pytest

from main_76 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert Solution().minWindow("ab", "a") == "a"
    assert Solution().minWindow("a", "a") == "a"
