import pytest

from main_1804 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().numDifferentIntegers("a123bc34d8ef34") == 3
    assert Solution().numDifferentIntegers("leet1234code234") == 2
    assert Solution().numDifferentIntegers("a1b01c001") == 1
