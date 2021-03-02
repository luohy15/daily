class Solution(object):
    """
    brute force:
        res[0] = 0
        res[1] = 1
        res[n] = res[n - 1] + res[n - 2]
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
            ai = ai1 + ai2
            ai2 = ai1
            ai1 = ai
        return ai