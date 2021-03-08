import pytest

from main_189 import Solution

def test1():
    nums = [1,2,3,4,5,6,7]
    k = 3
    Solution().rotate(nums, k)
    assert nums == [5,6,7,1,2,3,4]

def test2():
    nums = [-1,-100,3,99]
    k = 2
    Solution().rotate(nums, k)
    assert nums == [3,99,-1,-100]
