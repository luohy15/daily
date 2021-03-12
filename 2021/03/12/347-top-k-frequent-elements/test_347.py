import pytest

from main_347 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    nums = [1,1,1,2,2,3]
    k = 2
    assert Solution().topKFrequent(nums, k) == [1,2]
