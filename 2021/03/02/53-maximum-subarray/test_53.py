import pytest

from main_53 import Solution as Solution0
from main_53_1 import Solution as Solution1

@pytest.fixture(params=[Solution0, Solution1])
def Solution(request):
    return request.param

def test1(Solution):
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    assert 6 == Solution().maxSubArray(nums)

def test2(Solution):
    nums = [1]
    assert 1 == Solution().maxSubArray(nums)