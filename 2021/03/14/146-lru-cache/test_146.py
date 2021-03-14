import pytest

from main_146 import LRUCache as Solution0
from main_146_1 import LRUCache as Solution1
from main_146_2 import LRUCache as Solution2

@pytest.fixture(params=[Solution0, Solution1, Solution2])
def Solution(request):
    return request.param

def test1(Solution):
    lRUCache = Solution(2)
    lRUCache.put(1, 1)
    lRUCache.put(2, 2)
    assert lRUCache.get(1) == 1
    lRUCache.put(3, 3)
    assert lRUCache.get(2) == -1
    lRUCache.put(4, 4)
    assert lRUCache.get(1) == -1
    assert lRUCache.get(3) == 3
    assert lRUCache.get(4) == 4