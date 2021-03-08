import pytest

from main_54 import Solution

def test1():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    assert Solution().spiralOrder(matrix) == [1,2,3,6,9,8,7,4,5]
