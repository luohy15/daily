import pytest

from main_75 import Solution as Solution0
from main_75_1 import Solution as Solution1

@pytest.fixture(params=[Solution0, Solution1])
def Solution(request):
    return request.param

def test1(Solution):
    nums = [2,0,2,1,1,0]
    Solution().sortColors(nums)
    assert nums == [0,0,1,1,2,2]

def test2(Solution):
    nums = [2,0,1]
    Solution().sortColors(nums)
    assert nums == [0,1,2]

def test3(Solution):
    nums = [0]
    Solution().sortColors(nums)
    assert nums == [0]

def test4(Solution):
    nums = [1]
    Solution().sortColors(nums)
    assert nums == [1]
    
def test5(Solution):
    nums = [2,1]
    Solution().sortColors(nums)
    assert nums == [1,2]

def test6(Solution):
    nums = [1,2,0]
    Solution().sortColors(nums)
    assert nums == [0,1,2]