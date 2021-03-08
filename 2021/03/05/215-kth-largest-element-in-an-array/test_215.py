import pytest

from main_215 import Solution as Solution0
from main_215_1 import Solution as Solution1

@pytest.fixture(params=[Solution0, Solution1])
def Solution(request):
    return request.param

def test1(Solution):
    nums = [3,2,1,5,6,4]
    k = 2
    assert Solution().findKthLargest(nums, k) == 5

def test2(Solution):
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    assert Solution().findKthLargest(nums, k) == 4
