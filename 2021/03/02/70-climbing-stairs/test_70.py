import unittest

# from main_70 import Solution
# from main_70_1 import Solution
from main_70_2 import Solution

def test1():
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(4) == 5

def test2():
    Solution().climbStairs(2)

if __name__ == "__main__":
    test2()