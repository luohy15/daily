import pytest

from main import Solution as Solution0
import sys
sys.path.append("./")
from lib.list import arr2list, list2arr

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    pass
