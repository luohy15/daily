import unittest

from main_200 import Solution
from main_200_1 import Solution
from main_200_2 import Solution

def test1():
    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert Solution().numIslands(grid) == 1

def test2():
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert Solution().numIslands(grid) == 3