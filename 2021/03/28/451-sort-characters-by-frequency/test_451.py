import pytest

from main_451 import Solution as Solution0
from main_451_1 import Solution as Solution1

@pytest.fixture(params=[Solution0, Solution1])
def Solution(request):
    return request.param

def test1(Solution):
    res = Solution().frequencySort("tree")
    assert res == "eetr" or res == "eert"
