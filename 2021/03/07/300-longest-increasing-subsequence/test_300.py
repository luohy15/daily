import unittest

from main_300 import Solution

def test1():
    nums = [10,9,2,5,3,7,101,18]
    assert Solution().lengthOfLIS(nums) == 4

def test2():
    nums = [0,1,0,3,2,3]
    assert Solution().lengthOfLIS(nums) == 4

def test3():
    nums = [7,7,7,7,7,7,7]
    assert Solution().lengthOfLIS(nums) == 1
