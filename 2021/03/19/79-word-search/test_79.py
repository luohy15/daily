import pytest

from main_79 import Solution as Solution0

@pytest.fixture(params=[Solution0])
def Solution(request):
    return request.param

def test1(Solution):
    board =[
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    assert Solution().exist(board, "ABCCED") == True

def test2(Solution):
    board =[
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    assert Solution().exist(board, "SEE") == True

def test3(Solution):
    board =[
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    assert Solution().exist(board, "ABCB") == False
