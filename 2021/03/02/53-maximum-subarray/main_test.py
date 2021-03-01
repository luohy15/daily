import unittest

from main import Solution
from main1 import Solution

class TestMain(unittest.TestCase):

    def test_1(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(6, Solution().maxSubArray(nums))

    def test_2(self):
        nums = [1]
        self.assertEqual(1, Solution().maxSubArray(nums))

if __name__ == '__main__':
    unittest.main()