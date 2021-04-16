def mult(ma, mb):
    f = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            f[i][j] = ma[i][0] * mb[0][j] + ma[i][1] * mb[1][j]
    return f

def fastpow(n):
    f = [[1, 0], [0, 1]]
    tmpm = [[1, 1], [1, 0]]
    while(n > 0):
        if n % 2 == 1:
            f = mult(f, tmpm)
        tmpm = mult(tmpm, tmpm)
        n = int(n / 2)
    return f

class Solution(object):
    """
    matrix fast power:
        f[-1] = 0
        f[0] = 1
        f[1] = 1
        f[n + 1] = f[n] + f[n - 1]

        [f[n + 1], f[n]]
            = [f[n] + f[n - 1], f[n]]
            = [[1, 1], [1, 0]] * [f[n], f[n - 1]]
            = [[1, 1], [1, 0]] ** (n + 1) * [f[0], f[-1]]
            = [[1, 1], [1, 0]] ** (n + 1) * [1, 0]
            = pow(matrix, n + 1) * [1, 0]

        f[n] = power(matrix, n)[0][0]
    time: O(logn)
    space: O(1)
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return fastpow(n)[0][0]
