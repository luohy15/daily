import pytest

from main_1806 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().reinitializePermutation(2) == 1
    assert Solution().reinitializePermutation(4) == 2
    assert Solution().reinitializePermutation(6) == 4
    assert Solution().reinitializePermutation(100000000) == 15300
