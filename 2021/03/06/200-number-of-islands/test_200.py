import pytest

from main_200 import Solution as Solution0
from main_200_1 import Solution as Solution1
from main_200_2 import Solution as Solution2

@pytest.fixture(params=[Solution0, Solution1, Solution2])
def Solution(request):
    return request.param

def test1(Solution):
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert Solution().numIslands(grid) == 1

def test2(Solution):
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert Solution().numIslands(grid) == 3