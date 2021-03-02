class Solution(object):
    """
    brute force:
        f[0] = 1
        f[1] = 1
        f[n] = f[n - 1] + f[n - 2]
    time: O(n)
    space: O(1)
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ai2 = 0
        ai1 = 0
        ai = 1
        # start from 1
        for i in range(1, n + 1):
            ai2 = ai1
            ai1 = ai
            ai = ai1 + ai2
        return ai