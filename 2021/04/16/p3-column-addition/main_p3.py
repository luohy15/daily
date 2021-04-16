from typing import List

def trans(s, n):
    return list(map(lambda x: int(x), [c for c in s.zfill(n)[::-1]]))

def ok(a, b, c, i):
    return a[i] + b[i] == c[i]

def carry(a, b, c, i):
    return a[i] + b[i] == c[i] + 10

def okWithCarry(a, b, c, i):
    return a[i] + b[i] + 1 == c[i]

def carryWithCarry(a, b, c, i):
    return a[i] + b[i] + 1 == c[i] + 10

class Solution(object):
    """
    状态：正确的算式的长度
    维度：当前位是否有进位，当前已用多少位
    转移方程
    dp(0, i) = max(dp(0, i - 1) + (a[i] + b[i] == c[i] ? 1 : 0),  a[i] + b[i] + 1 == c[i] ? dp(1, i - 1) + 1 : 0)
    dp(1, i) = max(a[i] + b[i] == c[i] + 10 ? dp(0, i - 1) + 1 : 0, dp(1, i - 1) + (a[i] + b[i] + 1 == c[i] + 10 ? 1 : 0))
    边界情况
    dp(0, 0) = a[0] + b[0] == c[0] ? 1 : 0
    dp(1, 0) = a[0] + b[0] == c[0] + 10 ? 1 : 0
    时间：O(n)
    空间：O(n)
    """
    def removeColumn(self, a, b, c):
        n = max(len(a), len(b), len(c))
        if n <= 0:
            return 0
        a = trans(a, n)
        b = trans(b, n)
        c = trans(c, n)
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = 1 if ok(a, b, c, 0) else 0
        dp[1][0] = 1 if carry(a, b, c, 0) else 0
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] + (1 if ok(a, b, c, i) else 0)
            dp[1][i] = (dp[0][i - 1] + 1) if carry(a, b, c, i) else 0
            if dp[1][i - 1]:
                dp[0][i] = max(dp[0][i], (dp[1][i - 1] + 1) if okWithCarry(a, b, c, i) else 0)
                dp[1][i] = max(dp[1][i], dp[1][i - 1] + (1 if carryWithCarry(a, b, c, i) else 0))
        return n - dp[0][n - 1]
