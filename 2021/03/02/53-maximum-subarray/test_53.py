import unittest

from main_53 import Solution
from main_53_1 import Solution

def test1():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    assert 6 == Solution().maxSubArray(nums)

def test2():
    nums = [1]
    assert 1 == Solution().maxSubArray(nums)