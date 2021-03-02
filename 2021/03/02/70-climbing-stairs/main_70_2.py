import math

class Solution(object):
    """
    fib: f[n] = (pow((1+sqrt5)/2, n)-pow((1-sqrt5)/2, n)) / sqrt5
    this problem: f[n] = (pow((1+sqrt5)/2, n + 1)-pow((1-sqrt5)/2, n + 1)) / sqrt5
    time: O(n)
    space: O(1)
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqrt5 = math.sqrt(5)
        return int((pow((1+sqrt5)/2, n+1)-pow((1-sqrt5)/2, n+1)) / sqrt5)