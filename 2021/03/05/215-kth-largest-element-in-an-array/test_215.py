import unittest

from main_215 import Solution
from main_215_1 import Solution

def test1():
    nums = [3,2,1,5,6,4]
    k = 2
    assert Solution().findKthLargest(nums, k) == 5

def test2():
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    assert Solution().findKthLargest(nums, k) == 4
