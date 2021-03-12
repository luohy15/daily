import pytest

from main_912 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    assert Solution().sortArray([5,2,3,1]) == [1,2,3,5]
    assert Solution().sortArray([5,1,1,2,0,0]) == [0,0,1,1,2,5]
