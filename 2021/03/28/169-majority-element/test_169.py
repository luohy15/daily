import pytest

from main_169 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().majorityElement([3,2,3]) == 3
    assert Solution().majorityElement([2,2,1,1,1,2,2]) == 2
