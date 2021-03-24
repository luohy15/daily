import pytest

from main_210 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().findOrder(2, [[1,0]]) == [0,1]

def test2(Solution):
    res = Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
    assert res == [0,1,2,3] or res == [0,2,1,3]

def test3(Solution):
    assert Solution().findOrder(2, [[1,0], [0,1]]) == []