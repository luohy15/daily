import pytest

from main_70 import Solution as Solution0
from main_70_1 import Solution as Solution1
from main_70_2 import Solution as Solution2

@pytest.fixture(params=[Solution0, Solution1, Solution2])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(4) == 5

def test2(Solution):
    Solution().climbStairs(2)
