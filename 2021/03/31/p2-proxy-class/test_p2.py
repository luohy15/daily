import pytest

from main_p2 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

class Hello(object):
    def __init__(self, name):
        self.name = name

    def hello(self):
        return self.name

def test1(Solution):
    h = Hello('world')
    p = Solution().generateProxy(h)
    assert p.hello() == 'world'
    print(p.name)
    p.name  = 'jobs'
    assert p.hello() == 'jobs'
